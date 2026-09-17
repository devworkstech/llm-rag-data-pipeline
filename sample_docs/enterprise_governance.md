# Enterprise Data Platform Governance

## 1. Medallion Architecture Principles
- **Bronze**: Append-only immutable ingestion.
- **Silver**: Deduplicated, cleansed, and validated data contracts.
- **Gold**: Business dimensional marts ready for BI and AI consumption.

## 2. Access Control & RBAC
All user queries must authenticate via IAM roles with column-level masking for PII/PHI.
