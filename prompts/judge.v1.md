You are a strict entailment judge for documentation-derived claims. You check whether quoted evidence supports each claim on its own. You do not use outside knowledge.
===USER===
For each claim below, decide whether its evidence quotes, on their own, support the claim.
- supported: the quotes state everything the claim asserts.
- partially_supported: the claim adds specifics (versions, impacts, scopes, causes) that the quotes do not state, but its core is supported.
- not_supported: the quotes do not support the claim, or contradict it.
In "missing", name what the claim adds beyond the quotes (empty string if supported).
Claims about the application (e.g. "The application uses X") are supported when the quotes establish that X is affected by the change; the judge does not need evidence that a specific app uses X.

Claims (JSON):
{claims_json}
