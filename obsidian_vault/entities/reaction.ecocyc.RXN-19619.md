---
entity_id: "reaction.ecocyc.RXN-19619"
entity_type: "reaction"
name: "RXN-19619"
source_database: "EcoCyc"
source_id: "RXN-19619"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19619

`reaction.ecocyc.RXN-19619`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19619`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

TRIMETHYLAMINE + an-oxidized-TorY-protein + WATER -> TRIMETHYLAMINE-N-O + A-REDUCED-TORY-PROTEIN + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: TRIMETHYLAMINE + an-oxidized-TorY-protein + WATER -> TRIMETHYLAMINE-N-O + A-REDUCED-TORY-PROTEIN + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by torZ (protein.P46923). Substrates: H2O (molecule.C00001), Trimethylamine (molecule.C00565). Products: H+ (molecule.C00080), Trimethylamine N-oxide (molecule.C01104).

## Annotation

TRIMETHYLAMINE + an-oxidized-TorY-protein + WATER -> TRIMETHYLAMINE-N-O + A-REDUCED-TORY-PROTEIN + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P46923|protein.P46923]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01104|molecule.C01104]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00565|molecule.C00565]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[protein.P18775|protein.P18775]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-19619`

## Notes

TRIMETHYLAMINE + an-oxidized-TorY-protein + WATER -> TRIMETHYLAMINE-N-O + A-REDUCED-TORY-PROTEIN + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
