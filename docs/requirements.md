# KnowledgeAxis / Requirements

Independent public portfolio lab. NSA public Zero Trust guidance informs selected security controls; no NSA-specific knowledge graph standard, approval, accreditation, or operational equivalence is established. Neo4j is a property graph, not a native RDF/OWL reasoner. PUBLIC-DEMO is a local tag, not an official government classification.

| Capability | Area | Evidence | Status |
|---|---|---|---|
| 4.1 | Data inventory | JSON/CSV graph inventory with unique IDs | Implemented in dataset; automated discovery absent |
| 4.2 | Governance | Source and status fields; publication policy | Partial; no enterprise governance service |
| 4.3 | Data tagging | Public portfolio classification and provenance | Partial; tags are metadata, not authorization |
| 4.4 | Monitoring | Import output and validation tests | Partial; database activity monitoring not implemented |
| 4.5 | Encryption | Encrypted EBS; SSM tunnel; loopback ports | Partial; no application TLS or rights management |
| 4.6 | Loss prevention | Public-only export policy | Manual policy; no DLP engine |
| 4.7 | Access control | No inbound security-group rules; database authentication | Partial; no attribute-based authorization |
| 7.1 | Logging | Deployment and ingestion logs | Partial; no centralized security telemetry |
| 7.2 | SIEM | Proposed centralized log collection | Not implemented |

## References
https://www.nsa.gov/Cybersecurity/ZIG/Pillars/Data-Pillar/
https://www.nsa.gov/Cybersecurity/ZIG/Capabilities/Data/
https://www.nsa.gov/Cybersecurity/ZIG/Pillars/Visibility-and-Analytics-Pillar/
https://www.w3.org/TR/prov-o/
https://neo4j.com/docs/cypher-manual/current/

## Acceptance gates
- Unique node IDs and valid relationship endpoints.
- No credentials or nonpublic data in published files.
- Run local Neo4j import and verify counts.
- Deploy AWS lab, inspect ingress and encrypted volumes, test SSM access.
- Production authorization, TLS, auditing, backup restore and policy enforcement require separate implementation and review.
