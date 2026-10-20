"""Data model. Assignment fields and enums (TDD 6.1) are kept exactly; extensions per 6.2 / 17."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

RiskType = Literal[
    "removed_api", "changed_behavior", "changed_default", "dependency_requirement",
    "runtime_requirement", "configuration_change", "data_migration", "operational_risk", "unknown",
]
RiskLevel = Literal["critical", "high", "medium", "low", "unknown"]
Surface = Literal[
    "application_code", "configuration", "dependencies", "runtime", "database", "deployment", "tests", "unknown",
]
Category = Literal[
    "version", "api_usage", "configuration", "dependency", "runtime", "deployment", "database",
    "behavior", "test_coverage", "unknown",
]
Operator = Literal[
    "equals", "not_equals", "in_range", "less_than", "greater_than", "contains", "absent", "present", "unknown",
]
Confidence = Literal["high", "medium", "low"]
Role = Literal["required", "alternative", "optional", "disqualifying", "uncertain"]
DerivedBy = Literal["extraction", "rule", "inference"]
FiresAt = Literal["upgrade", "first_use", "rotation", "rollout", "future_removal"]
SourceType = Literal[
    "official_release_notes", "official_migration_guide", "official_changelog", "official_deprecation_notice",
    "official_api_docs", "package_registry_metadata", "github_issue", "maintainer_blog", "community_writeup",
]
SectionType = Literal["removed", "deprecated", "incompatible", "changed", "new", "requirements", "urgent", "other"]
JudgeVerdict = Literal["supported", "partially_supported", "not_supported"]

APP_SIDE_CATEGORIES = {
    "api_usage", "configuration", "dependency", "runtime", "deployment", "database", "behavior", "test_coverage",
}
LEVEL_ORDER = ["unknown", "low", "medium", "high", "critical"]


class _M(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Evidence(_M):
    source_id: str
    source_type: SourceType
    quote_or_summary: str
    relevance: str
    quote: str | None = None
    verified: bool = False
    json_path: str | None = None
    expected: str | None = None


class SearchQuery(_M):
    tool: Literal["ripgrep", "kubectl", "sql"]
    query: str


class JudgeResult(_M):
    verdict: JudgeVerdict
    missing: str = ""


class Condition(_M):
    condition_id: str
    statement: str
    category: Category
    required: bool
    operator: Operator
    expected_value: str | dict[str, Any] | list[Any]
    evidence: list[Evidence]
    confidence: Confidence
    ambiguities: list[str] = Field(default_factory=list)
    role: Role = "required"
    derived_by: DerivedBy = "extraction"
    search_queries: list[SearchQuery] = Field(default_factory=list)
    judge: JudgeResult | None = None


class AppliesTo(_M):
    cluster_type: str | None = None
    upgrade_method: str | None = None
    from_versions: str | None = None


class RiskPath(_M):
    path_id: str
    path_name: str
    risk_type: RiskType
    risk_level: RiskLevel
    affected_surface: Surface
    description: str
    conditions: list[Condition]
    suggested_actions: list[str]
    confidence: Confidence = "low"
    applies_to: AppliesTo | None = None
    fires_at: FiresAt = "upgrade"
    introduced_in: str = "*"
    primary_symbol: str = ""
    symbols: list[str] = Field(default_factory=list)
    superseded_by: str | None = None
    reverted_in: str | None = None
    merged_from: list[str] = Field(default_factory=list)
    source_item_ids: list[str] = Field(default_factory=list)
    review_status: Literal["unreviewed", "accepted", "edited"] = "unreviewed"
    review_flags: list[str] = Field(default_factory=list)


class ContextFact(_M):
    fact_id: str
    statement: str
    introduced_in: str
    evidence: list[Evidence]
    why_not_risk: str
    fires_at: FiresAt | None = None


class DisqualifiedCandidate(_M):
    candidate_id: str
    statement: str
    reason: str
    evidence: list[Evidence]


class RequiresUpgrade(_M):
    project: str
    current_version: str
    target_version: str
    reason: str
    evidence: list[Evidence]
    model_ref: str


class SourceRecord(_M):
    source_id: str
    title: str
    url: str
    source_type: SourceType
    retrieved_at: str
    why_relevant: str
    authority_tier: int
    content_hash: str = ""
    pinned_ref: str = ""
    status: Literal["used", "rejected"] = "used"
    rejection_reason: str | None = None
    release: str | None = None
    raw_url: str = ""
    registry_source: str = ""


class Disagreement(_M):
    topic: str
    sources: list[str]
    detail: str
    resolution: str


class EvidenceSummary(_M):
    high_confidence_risks: list[str]
    medium_confidence_risks: list[str]
    low_confidence_or_disputed_risks: list[str]
    sources_with_disagreements: list[Disagreement]
    open_questions: list[str]


class RiskModel(_M):
    project: str
    current_version: str
    target_version: str
    upgrade: str
    disclaimer: str
    summary: str
    source_inventory: list[SourceRecord]
    risk_paths: list[RiskPath]
    open_questions: list[str]
    overall_confidence: Confidence
    evidence_summary: EvidenceSummary
    context_facts: list[ContextFact] = Field(default_factory=list)
    disqualified_candidates: list[DisqualifiedCandidate] = Field(default_factory=list)
    requires_upgrades: list[RequiresUpgrade] = Field(default_factory=list)
    plan: dict[str, Any] = Field(default_factory=dict)
    pipeline: dict[str, Any] = Field(default_factory=dict)


# ---------- internal models (TDD 6.3) ----------


class ChangeItem(_M):
    item_id: str
    project: str
    release: str
    source_id: str          # inventory id, e.g. "dj_notes@4.0"
    registry_source: str    # registry id, e.g. "dj_notes"
    heading_path: list[str]
    section_type: SectionType
    text: str
    raw_span: tuple[int, int]
    symbols: list[str]
    parent_id: str | None = None
    revert_candidate: bool = False
    also_in: list[str] = Field(default_factory=list)


class TriageLabel(_M):
    item_id: str
    label: Literal["risk", "context", "noise"]
    reason: str
    swept: bool = False


class VersionFact(_M):
    release: str
    field: str
    value: str
    source_id: str
    json_path: str
