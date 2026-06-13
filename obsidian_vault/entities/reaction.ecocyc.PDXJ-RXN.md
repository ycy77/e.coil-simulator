---
entity_id: "reaction.ecocyc.PDXJ-RXN"
entity_type: "reaction"
name: "PDXJ-RXN"
source_database: "EcoCyc"
source_id: "PDXJ-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PDXJ-RXN

`reaction.ecocyc.PDXJ-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PDXJ-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-AMINO-PROPAN-2-ONE-3-PHOSPHATE + DEOXYXYLULOSE-5P -> PROTON + PYRIDOXINE-5P + Pi + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 1-AMINO-PROPAN-2-ONE-3-PHOSPHATE + DEOXYXYLULOSE-5P -> PROTON + PYRIDOXINE-5P + Pi + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyridoxine 5'-phosphate synthase (complex.ecocyc.CPLX0-321). Substrates: 1-Deoxy-D-xylulose 5-phosphate (molecule.C11437), 3-Amino-2-oxopropyl phosphate (molecule.C11638). Products: H2O (molecule.C00001), H+ (molecule.C00080), Pyridoxine phosphate (molecule.C00627), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Annotation

1-AMINO-PROPAN-2-ONE-3-PHOSPHATE + DEOXYXYLULOSE-5P -> PROTON + PYRIDOXINE-5P + Pi + WATER; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-321|complex.ecocyc.CPLX0-321]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00627|molecule.C00627]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C11437|molecule.C11437]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11638|molecule.C11638]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PDXJ-RXN`

## Notes

1-AMINO-PROPAN-2-ONE-3-PHOSPHATE + DEOXYXYLULOSE-5P -> PROTON + PYRIDOXINE-5P + Pi + WATER; direction=LEFT-TO-RIGHT
