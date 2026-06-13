---
entity_id: "reaction.ecocyc.RXN-13179"
entity_type: "reaction"
name: "RXN-13179"
source_database: "EcoCyc"
source_id: "RXN-13179"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13179

`reaction.ecocyc.RXN-13179`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13179`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

4-PHOSPHONOOXY-THREONINE + NAD -> 1-AMINO-PROPAN-2-ONE-3-PHOSPHATE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 4-PHOSPHONOOXY-THREONINE + NAD -> 1-AMINO-PROPAN-2-ONE-3-PHOSPHATE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 4-hydroxythreonine-4-phosphate dehydrogenase (complex.ecocyc.CPLX0-7847). Substrates: NAD+ (molecule.C00003), O-Phospho-4-hydroxy-L-threonine (molecule.C06055). Products: NADH (molecule.C00004), CO2 (molecule.C00011), 3-Amino-2-oxopropyl phosphate (molecule.C11638).

## Enriched Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Annotation

4-PHOSPHONOOXY-THREONINE + NAD -> 1-AMINO-PROPAN-2-ONE-3-PHOSPHATE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7847|complex.ecocyc.CPLX0-7847]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11638|molecule.C11638]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06055|molecule.C06055]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13179`

## Notes

4-PHOSPHONOOXY-THREONINE + NAD -> 1-AMINO-PROPAN-2-ONE-3-PHOSPHATE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT
