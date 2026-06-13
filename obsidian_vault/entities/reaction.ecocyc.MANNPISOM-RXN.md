---
entity_id: "reaction.ecocyc.MANNPISOM-RXN"
entity_type: "reaction"
name: "MANNPISOM-RXN"
source_database: "EcoCyc"
source_id: "MANNPISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MANNPISOM-RXN

`reaction.ecocyc.MANNPISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MANNPISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of mannose catabolism. EcoCyc reaction equation: CPD-15979 -> FRUCTOSE-6P; direction=REVERSIBLE. Part of mannose catabolism.

## Biological Role

Catalyzed by manA (protein.P00946). Substrates: D-mannopyranose 6-phosphate (molecule.ecocyc.CPD-15979). Products: β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P).

## Enriched Pathways

- `ecocyc.MANNCAT-PWY` D-mannose degradation I (EcoCyc)
- `ecocyc.PWY-5659` GDP-mannose biosynthesis (EcoCyc)

## Annotation

Part of mannose catabolism.

## Pathways

- `ecocyc.MANNCAT-PWY` D-mannose degradation I (EcoCyc)
- `ecocyc.PWY-5659` GDP-mannose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P00946|protein.P00946]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15979|molecule.ecocyc.CPD-15979]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-15157|molecule.ecocyc.CPD-15157]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MANNPISOM-RXN`

## Notes

CPD-15979 -> FRUCTOSE-6P; direction=REVERSIBLE
