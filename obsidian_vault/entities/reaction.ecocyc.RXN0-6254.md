---
entity_id: "reaction.ecocyc.RXN0-6254"
entity_type: "reaction"
name: "RXN0-6254"
source_database: "EcoCyc"
source_id: "RXN0-6254"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6254

`reaction.ecocyc.RXN0-6254`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6254`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15870 + CTP + PROTON -> CPD-23445 + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15870 + CTP + PROTON -> CPD-23445 + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mocA (protein.Q46810). Substrates: CTP (molecule.C00063), H+ (molecule.C00080), Molybdoenzyme molybdenum cofactor (molecule.C18237). Products: Diphosphate (molecule.C00013), Cytidylyl molybdenum cofactor (molecule.C21485).

## Enriched Pathways

- `ecocyc.PWY-6476` cytidylyl molybdenum cofactor biosynthesis (EcoCyc)

## Annotation

CPD-15870 + CTP + PROTON -> CPD-23445 + PPI; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6476` cytidylyl molybdenum cofactor biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.Q46810|protein.Q46810]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21485|molecule.C21485]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6254`

## Notes

CPD-15870 + CTP + PROTON -> CPD-23445 + PPI; direction=LEFT-TO-RIGHT
