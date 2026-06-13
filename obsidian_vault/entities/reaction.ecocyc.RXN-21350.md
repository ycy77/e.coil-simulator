---
entity_id: "reaction.ecocyc.RXN-21350"
entity_type: "reaction"
name: "RXN-21350"
source_database: "EcoCyc"
source_id: "RXN-21350"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21350

`reaction.ecocyc.RXN-21350`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21350`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-23250 + WATER -> CPD-23251 + 5-Phospho-terminated-DNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-23250 + WATER -> CPD-23251 + 5-Phospho-terminated-DNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nfi (protein.P68739). Substrates: H2O (molecule.C00001), a deoxyinosine in DNA (molecule.ecocyc.CPD-23250). Products: H+ (molecule.C00080), deoxyinosine-containing DNA after cleavage by EndoV (molecule.ecocyc.CPD-23251).

## Annotation

CPD-23250 + WATER -> CPD-23251 + 5-Phospho-terminated-DNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P68739|protein.P68739]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-23251|molecule.ecocyc.CPD-23251]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-23250|molecule.ecocyc.CPD-23250]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21350`

## Notes

CPD-23250 + WATER -> CPD-23251 + 5-Phospho-terminated-DNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
