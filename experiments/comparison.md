# Model configuration experiment

Upgrades: react_17_to_18, postgresql_13_to_16, nextjs_12_to_14. Each config runs the full pipeline with its own cheap tier (triage) and strong tier (extraction, recall sweep, revert reconcile, grounding judge). Every config is scored with the same gold sets and the same Sonnet 5.5 precision judge; judge calibration uses the same claim set for every config.

| Config (cheap / strong) | Cost to produce | × cheapest | Paths | Gold recall | Est. precision | F1 | Strict precision | Classification | Level agreement | Judge acc. / κ | Stability | $ per gold risk found | Pareto |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haiku / Haiku | $0.27 | 1.0× | 115 | 53/55 (96.4%) | 99.1% | 0.977 | 67.8% | 96.5% | 98.1% | 1.000 / 1.000 | 0.742 | $0.005 | yes |
| Haiku / Sonnet | $3.25 | 12.1× | 110 | 54/55 (98.2%) | 99.1% | 0.986 | 65.5% | 98.2% | 100.0% | 1.000 / 1.000 | 0.700 (reused) | $0.060 | yes |
| Sonnet / Opus | $7.65 | 28.4× | 123 | 55/55 (100.0%) | 98.4% | 0.992 | 64.2% | 100.0% | 100.0% | 1.000 / 1.000 | 0.622 | $0.139 | yes |

Hard gates (grounding, validator errors) for every config: Haiku / Haiku: grounding 100.0%, 0 errors; Haiku / Sonnet: grounding 100.0%, 0 errors; Sonnet / Opus: grounding 100.0%, 0 errors

## Per upgrade

| Upgrade | Haiku / Haiku | Haiku / Sonnet | Sonnet / Opus |
|---|---|---|---|
| react_17_to_18 | 27 paths, recall 14/15, est. prec. 26/27, $0.09; missed re_render_to_node_stream | 25 paths, recall 14/15, est. prec. 24/25, $1.08; missed re_render_to_node_stream | 30 paths, recall 15/15, est. prec. 29/30, $2.71 |
| postgresql_13_to_16 | 69 paths, recall 27/28, est. prec. 69/69, $0.14; missed pg14_ssl_compression | 69 paths, recall 28/28, est. prec. 69/69, $1.67 | 79 paths, recall 28/28, est. prec. 78/79, $4.01 |
| nextjs_12_to_14 | 19 paths, recall 12/12, est. prec. 19/19, $0.04 | 16 paths, recall 12/12, est. prec. 16/16, $0.49 | 14 paths, recall 12/12, est. prec. 14/14, $0.93 |

Pareto = no other config is at least as cheap and at least as good on F1 (and strictly better on one).
Costs are list-price estimates from recorded token counts (prompt-caching discounts not modeled).
