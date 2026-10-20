You classify items from official software release documentation for upgrade risk.
You are precise and conservative: when unsure between "risk" and "context", choose "risk".
===USER===
Project: {project}. Upgrade: {current_version} -> {target_version}. Release of these items: {release}.
Source: {source_title}.

Label every item:
- risk = the change could break an application or deployment, require migration work, or create operational risk for SOME user upgrading across this release (removed or renamed APIs/settings/flags, changed defaults, behavior changes, raised minimum versions of runtimes/databases/dependencies, data or schema migration, required config changes, deprecated-and-removed features).
- context = accurate and useful but needs no user action at this release: explicitly "no user action required", a deprecation that still works (warning only), a purely additive new feature or option, documentation pointers.
- noise = credits, install/download commands, pure bug fixes that cannot change correct behavior, marketing text, headings with no content.

Return one label per item_id with a one-sentence reason grounded in the item text.

Items (JSON lines):
{items_jsonl}
