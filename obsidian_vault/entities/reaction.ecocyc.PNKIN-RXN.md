---
entity_id: "reaction.ecocyc.PNKIN-RXN"
entity_type: "reaction"
name: "PNKIN-RXN"
source_database: "EcoCyc"
source_id: "PNKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PNKIN-RXN

`reaction.ecocyc.PNKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PNKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyridoxal 5'-phosphate salvage pathway. It is an alternative substrate reaction of E.C.# 2.7.1.35. EcoCyc reaction equation: ATP + PYRIDOXINE -> PROTON + ADP + PYRIDOXINE-5P; direction=LEFT-TO-RIGHT. This reaction is part of the pyridoxal 5'-phosphate salvage pathway. It is an alternative substrate reaction of E.C.# 2.7.1.35.

## Biological Role

Catalyzed by pyridoxal kinase 1 / hydroxymethylpyrimidine kinase (complex.ecocyc.PDXK-CPLX). Substrates: ATP (molecule.C00002), Pyridoxine (molecule.C00314). Products: ADP (molecule.C00008), H+ (molecule.C00080), Pyridoxine phosphate (molecule.C00627).

## Enriched Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Annotation

This reaction is part of the pyridoxal 5'-phosphate salvage pathway. It is an alternative substrate reaction of E.C.# 2.7.1.35.

## Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.PDXK-CPLX|complex.ecocyc.PDXK-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00627|molecule.C00627]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00314|molecule.C00314]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01279|molecule.C01279]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1605|molecule.ecocyc.CPD0-1605]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PNKIN-RXN`

## Notes

ATP + PYRIDOXINE -> PROTON + ADP + PYRIDOXINE-5P; direction=LEFT-TO-RIGHT
