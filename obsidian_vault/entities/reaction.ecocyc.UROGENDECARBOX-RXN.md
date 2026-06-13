---
entity_id: "reaction.ecocyc.UROGENDECARBOX-RXN"
entity_type: "reaction"
name: "UROGENDECARBOX-RXN"
source_database: "EcoCyc"
source_id: "UROGENDECARBOX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UROGENDECARBOX-RXN

`reaction.ecocyc.UROGENDECARBOX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UROGENDECARBOX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in porphyrin biosynthesis. EcoCyc reaction equation: PROTON + UROPORPHYRINOGEN-III -> CARBON-DIOXIDE + COPROPORPHYRINOGEN_III; direction=LEFT-TO-RIGHT. A reaction in porphyrin biosynthesis.

## Biological Role

Catalyzed by hemE (protein.P29680). Substrates: H+ (molecule.C00080), Uroporphyrinogen III (molecule.C01051). Products: CO2 (molecule.C00011), Coproporphyrinogen III (molecule.C03263).

## Enriched Pathways

- `ecocyc.HEME-BIOSYNTHESIS-II-1` heme b biosynthesis V (aerobic) (EcoCyc)
- `ecocyc.HEMESYN2-PWY` heme b biosynthesis II (oxygen-independent) (EcoCyc)

## Annotation

A reaction in porphyrin biosynthesis.

## Pathways

- `ecocyc.HEME-BIOSYNTHESIS-II-1` heme b biosynthesis V (aerobic) (EcoCyc)
- `ecocyc.HEMESYN2-PWY` heme b biosynthesis II (oxygen-independent) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P29680|protein.P29680]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03263|molecule.C03263]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01051|molecule.C01051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UROGENDECARBOX-RXN`

## Notes

PROTON + UROPORPHYRINOGEN-III -> CARBON-DIOXIDE + COPROPORPHYRINOGEN_III; direction=LEFT-TO-RIGHT
