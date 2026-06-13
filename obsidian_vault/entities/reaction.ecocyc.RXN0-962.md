---
entity_id: "reaction.ecocyc.RXN0-962"
entity_type: "reaction"
name: "RXN0-962"
source_database: "EcoCyc"
source_id: "RXN0-962"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-962

`reaction.ecocyc.RXN0-962`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-962`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FRUCTOSELYSINE + ATP -> PROTON + FRUCTOSELYSINE-6-PHOSPHATE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FRUCTOSELYSINE + ATP -> PROTON + FRUCTOSELYSINE-6-PHOSPHATE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by frlD (protein.P45543). Substrates: ATP (molecule.C00002), Fructoselysine (molecule.C16488). Products: ADP (molecule.C00008), H+ (molecule.C00080), Fructoselysine 6-phosphate (molecule.C16489).

## Enriched Pathways

- `ecocyc.PWY0-521` fructoselysine and psicoselysine degradation (EcoCyc)

## Annotation

FRUCTOSELYSINE + ATP -> PROTON + FRUCTOSELYSINE-6-PHOSPHATE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-521` fructoselysine and psicoselysine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P45543|protein.P45543]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16489|molecule.C16489]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16488|molecule.C16488]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-962`

## Notes

FRUCTOSELYSINE + ATP -> PROTON + FRUCTOSELYSINE-6-PHOSPHATE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
