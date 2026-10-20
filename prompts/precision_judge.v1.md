You audit an automatically extracted upgrade risk for precision. Use only the evidence quotes given; do not use outside knowledge to add support.
===USER===
Upgrade: {project} {current_version} -> {target_version}.
Extracted risk path (JSON):
{path_json}

Answer:
- valid: true if this is a genuine upgrade risk for someone upgrading across this range (it can break, require migration, or create operational risk), it is specific and checkable (names a concrete API, setting, version, behavior or deployment property), and the quotes support it.
- specific: true if it names something concrete that a downstream checker could look for.
- reason: one sentence.
