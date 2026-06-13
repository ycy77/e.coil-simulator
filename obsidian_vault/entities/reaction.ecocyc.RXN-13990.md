---
entity_id: "reaction.ecocyc.RXN-13990"
entity_type: "reaction"
name: "L-4-hydroxy-2-oxoglutarate aldolase"
source_database: "EcoCyc"
source_id: "RXN-13990"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-4-hydroxy-2-oxoglutarate aldolase

`reaction.ecocyc.RXN-13990`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13990`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15016 -> GLYOX + PYRUVATE; direction=REVERSIBLE EcoCyc reaction equation: CPD-15016 -> GLYOX + PYRUVATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by KHG/KDPG aldolase (complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX). Substrates: (4S)-4-hydroxy-2-oxoglutarate (molecule.ecocyc.CPD-15016). Products: Pyruvate (molecule.C00022), Glyoxylate (molecule.C00048).

## Annotation

CPD-15016 -> GLYOX + PYRUVATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX|complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15016|molecule.ecocyc.CPD-15016]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00168|molecule.C00168]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.3-BROMOPYRUVATE|molecule.ecocyc.3-BROMOPYRUVATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1309|molecule.ecocyc.CPD0-1309]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-13990`

## Notes

CPD-15016 -> GLYOX + PYRUVATE; direction=REVERSIBLE
