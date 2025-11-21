# Case Studies — Failures & Remedies

## Case 1 — Biased recommendations (hypothetical)
**Problem:** Recommendation model amplifies historical bias.  
**Root cause:** Training data reflects legacy discrimination.  
**Mitigation:** reweighting in training, fairness constraint, manual audit of top-k recommendations.  
**Governance step:** block deployment until fairness score threshold met.

## Case 2 — Sensitive data leak in logs
**Problem:** Model logs inadvertently contained PII.  
**Root cause:** debug logging in prod without redaction.  
**Mitigation:** apply input-output redaction middleware; rotate logs; incident response.  
**Governance step:** require privacy sign-off before production telemetry.

## Case 3 — Over-automation causing regression
**Problem:** Auto-generated patches from code assistants introduced logic regressions.  
**Root cause:** insufficient test oracles for generated code.  
**Mitigation:** restrict auto-apply; require tests to run in preview; human review gating.
