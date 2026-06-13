---
entity_id: "reaction.ecocyc.ACYLGPEACYLTRANS-RXN"
entity_type: "reaction"
name: "ACYLGPEACYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "ACYLGPEACYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACYLGPEACYLTRANS-RXN

`reaction.ecocyc.ACYLGPEACYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACYLGPEACYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the acyl-CoA-independent incorporation of exogenous fatty acids and 2-acyllysophospholipids into the cell. EcoCyc reaction equation: ACYL-ACP + 2-ACYL-GPE -> ACP + L-1-PHOSPHATIDYL-ETHANOLAMINE; direction=REVERSIBLE. This reaction is part of the acyl-CoA-independent incorporation of exogenous fatty acids and 2-acyllysophospholipids into the cell.

## Biological Role

Catalyzed by aas (protein.P31119). Substrates: 2-Acyl-sn-glycero-3-phosphoethanolamine (molecule.C05973). Products: Phosphatidylethanolamine (molecule.C00350).

## Annotation

This reaction is part of the acyl-CoA-independent incorporation of exogenous fatty acids and 2-acyllysophospholipids into the cell.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P31119|protein.P31119]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05973|molecule.C05973]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACYLGPEACYLTRANS-RXN`

## Notes

ACYL-ACP + 2-ACYL-GPE -> ACP + L-1-PHOSPHATIDYL-ETHANOLAMINE; direction=REVERSIBLE
