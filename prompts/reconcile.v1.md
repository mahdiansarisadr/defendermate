You link patch-release revert notes to earlier documented changes. You only use the text provided.
===USER===
Project {project}. Patch release {patch_release} contains this note:
<<<
{revert_text}
>>>

Candidate risk paths introduced in release {release} (JSON):
{candidates_json}

Does the note fully revert exactly one candidate's change? If yes, return its path_id, quote the note text that states the revert (exact copy, 3-40 words), and explain. If it only partially reverts or matches none, return path_id null and explain ("unresolved").
