"""TDD 13.1: golden sentences per format adapter, plus normalizer properties."""

import re

from urx.adapters import doc_text, rst, window
from urx.adapters.markdown import convert_inline as md_inline
from urx.normalize import normalize

from conftest import blocks_of


def test_rst_setting_role():
    assert "CSRF_TRUSTED_ORIGINS" in normalize(rst.convert_inline(":setting:`CSRF_TRUSTED_ORIGINS`"))


def test_rst_labelled_role_shows_label():
    assert normalize(rst.convert_inline(":py:attr:`hostname <ssl.SSLContext.check_hostname>`")) == "hostname"


def test_rst_leading_dot_and_tilde():
    assert normalize(rst.convert_inline(":meth:`.Expression.get_group_by_cols`")) == "Expression.get_group_by_cols"
    assert normalize(rst.convert_inline(":func:`~django.utils.encoding.force_text`")) == "force_text"


def test_rst_django_4_0_has_csrf_and_removed_section():
    b = blocks_of("django/dj_notes/4.0.txt", "rst")
    text = doc_text(b)
    assert "Values in the CSRF_TRUSTED_ORIGINS setting must include the scheme" in text
    heads = [x.norm for x in b if x.kind == "heading"]
    assert "Features removed in 4.0" in heads and "Backwards incompatible changes in 4.0" in heads


def test_docbook_keeps_password_encryption():
    b = blocks_of("postgresql/pg_release_notes/14.sgml", "docbook")
    w = window(b, r"^Migration to Version 14$", None)
    t = " ".join(x.norm for x in w)
    assert "password_encryption" in t
    assert not re.search(r" ,|, ,| or use of or ", t)


def test_docbook_pg15_16_mention_pg_upgrade():
    for r in ("15", "16"):
        b = blocks_of(f"postgresql/pg_release_notes/{r}.sgml", "docbook")
        assert "pg_upgrade" in " ".join(x.norm for x in window(b, rf"^Migration to Version {r}$", None))


def test_docbook_exact_sect2_title_excludes_minor_releases():
    b = blocks_of("postgresql/pg_release_notes/14.sgml", "docbook")
    w = window(b, r"^Migration to Version 14$", None)
    assert w[0].norm == "Migration to Version 14"
    assert not any("14.2" in x.norm for x in w if x.kind == "heading")


def test_mdx_jsx_comments_removed():
    b = blocks_of("nextjs/next_guide_14_tag/doc.mdx", "mdx")
    assert "DO NOT EDIT" not in doc_text(b) and "content of this doc is shared" not in doc_text(b)


def test_markdown_keeps_code_span_tags():
    assert md_inline("The `next/link` child can no longer be `<a>`. Use <Foo>x</Foo>") == \
        "The `next/link` child can no longer be `<a>`. Use x"


def test_markdown_k8s_urgent_notes_dockershim_and_pr_refs_stripped():
    b = blocks_of("kubernetes/k8s_changelog/1.24.md", "markdown")
    scope = window(b, r"^v1\.24\.0$", r"^v1\.24\.0-")
    urgent = window(scope, r"^Urgent Upgrade Notes$", r"^Changes by Kind$")
    t = " ".join(x.norm for x in urgent)
    assert "dockershim" in t
    assert "github.com/kubernetes/kubernetes/pull" not in t and "[SIG" not in t


def test_react_section_boundaries_by_anchor_not_depth():
    b = blocks_of("react/react_changelog/doc.md", "markdown")
    w = window(b, r"^18\.0\.0 ", r"^17\.0\.2 ")
    heads = [x.norm for x in w if x.kind == "heading"]
    assert "Breaking Changes" in heads
    assert not any(h.startswith("17.0.2") for h in heads)


def test_normalizer_keeps_wildcard_urls_and_is_idempotent():
    s = "Use `https://*.example.com` and **bold** \u201cquotes\u201d\u00a0here\\n"
    n = normalize(s)
    assert "https://*.example.com" in n
    assert normalize(n) == n
    assert '"quotes"' in n
