---
entity_id: "reaction.ecocyc.ERYTH4PDEHYDROG-RXN"
entity_type: "reaction"
name: "ERYTH4PDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "ERYTH4PDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ERYTH4PDEHYDROG-RXN

`reaction.ecocyc.ERYTH4PDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ERYTH4PDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction may play a role in the de novo biosynthesis of the pyridoxal 5'-phosphate coenzyme. EcoCyc reaction equation: ERYTHROSE-4P + WATER + NAD -> ERYTHRONATE-4P + NADH + PROTON; direction=LEFT-TO-RIGHT. This reaction may play a role in the de novo biosynthesis of the pyridoxal 5'-phosphate coenzyme.

## Biological Role

Catalyzed by D-erythrose-4-phosphate dehydrogenase (complex.ecocyc.ERYTH4PDEHYDROG-CPLX). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), D-Erythrose 4-phosphate (molecule.C00279). Products: NADH (molecule.C00004), H+ (molecule.C00080), 4-Phospho-D-erythronate (molecule.C03393).

## Enriched Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Annotation

This reaction may play a role in the de novo biosynthesis of the pyridoxal 5'-phosphate coenzyme.

## Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ERYTH4PDEHYDROG-CPLX|complex.ecocyc.ERYTH4PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03393|molecule.C03393]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00279|molecule.C00279]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ERYTH4PDEHYDROG-RXN`

## Notes

ERYTHROSE-4P + WATER + NAD -> ERYTHRONATE-4P + NADH + PROTON; direction=LEFT-TO-RIGHT
