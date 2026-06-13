---
entity_id: "reaction.ecocyc.RXN-21858"
entity_type: "reaction"
name: "RXN-21858"
source_database: "EcoCyc"
source_id: "RXN-21858"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21858

`reaction.ecocyc.RXN-21858`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21858`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-14736 + 2-KETOGLUTARATE -> KYNURENATE + GLT + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-14736 + 2-KETOGLUTARATE -> KYNURENATE + GLT + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aspartate aminotransferase (complex.ecocyc.ASPAMINOTRANS-DIMER). Substrates: 2-Oxoglutarate (molecule.C00026), L-Kynurenine (molecule.C00328). Products: H2O (molecule.C00001), L-Glutamate (molecule.C00025), H+ (molecule.C00080), 4-Hydroxy-2-quinolinecarboxylic acid (molecule.C01717).

## Annotation

CPD-14736 + 2-KETOGLUTARATE -> KYNURENATE + GLT + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ASPAMINOTRANS-DIMER|complex.ecocyc.ASPAMINOTRANS-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01717|molecule.C01717]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00328|molecule.C00328]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01384|molecule.C01384]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1614|molecule.ecocyc.CPD0-1614]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-21858`

## Notes

CPD-14736 + 2-KETOGLUTARATE -> KYNURENATE + GLT + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
