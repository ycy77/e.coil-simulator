---
entity_id: "reaction.ecocyc.RXN0-7173"
entity_type: "reaction"
name: "RXN0-7173"
source_database: "EcoCyc"
source_id: "RXN0-7173"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7173

`reaction.ecocyc.RXN0-7173`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7173`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-8887 + WATER -> GLYCOLLATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-8887 + WATER -> GLYCOLLATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by protein/nucleic acid deglycase 3 (complex.ecocyc.CPLX0-7960), elbB (protein.P0ABU5). Substrates: H2O (molecule.C00001), glyoxal (molecule.ecocyc.CPD-8887). Products: H+ (molecule.C00080), Glycolate (molecule.C00160).

## Annotation

CPD-8887 + WATER -> GLYCOLLATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7960|complex.ecocyc.CPLX0-7960]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABU5|protein.P0ABU5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-8887|molecule.ecocyc.CPD-8887]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7173`

## Notes

CPD-8887 + WATER -> GLYCOLLATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
