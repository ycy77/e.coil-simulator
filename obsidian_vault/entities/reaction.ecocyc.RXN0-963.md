---
entity_id: "reaction.ecocyc.RXN0-963"
entity_type: "reaction"
name: "RXN0-963"
source_database: "EcoCyc"
source_id: "RXN0-963"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-963

`reaction.ecocyc.RXN0-963`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-963`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FRUCTOSELYSINE-6-PHOSPHATE + WATER -> GLC-6-P + LYS; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FRUCTOSELYSINE-6-PHOSPHATE + WATER -> GLC-6-P + LYS; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fructoselysine 6-phosphate deglycase (complex.ecocyc.CPLX0-821). Substrates: H2O (molecule.C00001), Fructoselysine 6-phosphate (molecule.C16489). Products: L-Lysine (molecule.C00047), beta-D-Glucose 6-phosphate (molecule.C01172).

## Enriched Pathways

- `ecocyc.PWY0-521` fructoselysine and psicoselysine degradation (EcoCyc)

## Annotation

FRUCTOSELYSINE-6-PHOSPHATE + WATER -> GLC-6-P + LYS; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-521` fructoselysine and psicoselysine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.EGTA|molecule.ecocyc.EGTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-821|complex.ecocyc.CPLX0-821]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01172|molecule.C01172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16489|molecule.C16489]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-963`

## Notes

FRUCTOSELYSINE-6-PHOSPHATE + WATER -> GLC-6-P + LYS; direction=LEFT-TO-RIGHT
