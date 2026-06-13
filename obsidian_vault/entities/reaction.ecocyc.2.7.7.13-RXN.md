---
entity_id: "reaction.ecocyc.2.7.7.13-RXN"
entity_type: "reaction"
name: "2.7.7.13-RXN"
source_database: "EcoCyc"
source_id: "2.7.7.13-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "ATP-mannose-1-phosphate guanylyltransferase"
---

# 2.7.7.13-RXN

`reaction.ecocyc.2.7.7.13-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.7.13-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + MANNOSE-1P + GTP -> GDP-MANNOSE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + MANNOSE-1P + GTP -> GDP-MANNOSE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by manC (protein.P24174). Substrates: GTP (molecule.C00044), H+ (molecule.C00080), D-Mannose 1-phosphate (molecule.C00636). Products: Diphosphate (molecule.C00013), GDP-mannose (molecule.C00096).

## Enriched Pathways

- `ecocyc.PWY-5659` GDP-mannose biosynthesis (EcoCyc)

## Annotation

PROTON + MANNOSE-1P + GTP -> GDP-MANNOSE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5659` GDP-mannose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P24174|protein.P24174]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00096|molecule.C00096]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00636|molecule.C00636]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.7.7.13-RXN`

## Notes

PROTON + MANNOSE-1P + GTP -> GDP-MANNOSE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
