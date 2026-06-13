---
entity_id: "reaction.ecocyc.PYRIDOXKIN-RXN"
entity_type: "reaction"
name: "PYRIDOXKIN-RXN"
source_database: "EcoCyc"
source_id: "PYRIDOXKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PYRODOXINE KINASE"
  - "PYRODOXAMINE KINASE"
  - "VITAMIN B6 KINASE"
---

# PYRIDOXKIN-RXN

`reaction.ecocyc.PYRIDOXKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRIDOXKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyridoxal 5'-phosphate salvage pathway. EcoCyc reaction equation: ATP + PYRIDOXAL -> PROTON + ADP + PYRIDOXAL_PHOSPHATE; direction=LEFT-TO-RIGHT. This reaction is part of the pyridoxal 5'-phosphate salvage pathway.

## Biological Role

Catalyzed by pyridoxal kinase 2 (complex.ecocyc.CPLX0-8031), pyridoxal kinase 1 / hydroxymethylpyrimidine kinase (complex.ecocyc.PDXK-CPLX). Substrates: ATP (molecule.C00002), Pyridoxal (molecule.C00250). Products: ADP (molecule.C00008), Pyridoxal phosphate (molecule.C00018), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Annotation

This reaction is part of the pyridoxal 5'-phosphate salvage pathway.

## Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8031|complex.ecocyc.CPLX0-8031]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.PDXK-CPLX|complex.ecocyc.PDXK-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00250|molecule.C00250]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00250|molecule.C00250]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1408|molecule.ecocyc.CPD0-1408]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1605|molecule.ecocyc.CPD0-1605]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PYRIDOXKIN-RXN`

## Notes

ATP + PYRIDOXAL -> PROTON + ADP + PYRIDOXAL_PHOSPHATE; direction=LEFT-TO-RIGHT
