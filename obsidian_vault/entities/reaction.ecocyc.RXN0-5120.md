---
entity_id: "reaction.ecocyc.RXN0-5120"
entity_type: "reaction"
name: "RXN0-5120"
source_database: "EcoCyc"
source_id: "RXN0-5120"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5120

`reaction.ecocyc.RXN0-5120`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5120`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12575 + CPD0-930 -> PROTON + CPD0-932 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12575 + CPD0-930 -> PROTON + CPD0-932 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaG (protein.P25740). Substrates: UDP-glucose (molecule.C00029), α-Hep-(1→3)-α-Hep-(1→5)-[α-Kdo-(2→4)]-α-Kdo-(2→6)-lipid A (E. coli) (molecule.ecocyc.CPD0-930). Products: UDP (molecule.C00015), H+ (molecule.C00080), glucosyl-(heptosyl)2-Kdo2-lipid A (molecule.ecocyc.CPD0-932).

## Annotation

CPD-12575 + CPD0-930 -> PROTON + CPD0-932 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[protein.P25740|protein.P25740]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-932|molecule.ecocyc.CPD0-932]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-930|molecule.ecocyc.CPD0-930]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5120`

## Notes

CPD-12575 + CPD0-930 -> PROTON + CPD0-932 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
