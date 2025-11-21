# Responsibility Guidelines (Engineering Teams)

## Roles & Responsibilities
- **Product Owner**: defines high-level acceptable use cases.  
- **Model Owner**: owns the model lifecycle.  
- **Data Steward**: ensures data quality and compliance.  
- **Security/Privacy Lead**: approves deployments with data access.  
- **Ethics Reviewer**: independent review of high-risk features.

## Engineering controls
- Access controls on model training datasets.  
- Canary releases, gradual rollouts and rollback paths.  
- Sandbox environments for model testing.  
- Logging of model inputs/outputs respecting privacy policies.

## Governance meetings
- Weekly squad sync for low-risk features.  
- Bi-weekly cross-functional ethics review for medium-risk.  
- Quarterly governance board for high-risk projects.

## Example policy snippets
- Require an ethics sign-off for features with user impact > medium.  
- Mandatory data provenance attached to any training dataset.
