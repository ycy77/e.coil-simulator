---
entity_id: "reaction.ecocyc.RXN-17809"
entity_type: "reaction"
name: "RXN-17809"
source_database: "EcoCyc"
source_id: "RXN-17809"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17809

`reaction.ecocyc.RXN-17809`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17809`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19179 -> PRECURSOR-Z + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-19179 -> PRECURSOR-Z + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cyclic pyranopterin monophosphate synthase (complex.ecocyc.CPLX-8331). Substrates: (8S)-3',8-Cyclo-7,8-dihydroguanosine 5'-triphosphate (molecule.C21310). Products: Diphosphate (molecule.C00013), cyclic pyranopterin phosphate (molecule.ecocyc.PRECURSOR-Z).

## Enriched Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Annotation

CPD-19179 -> PRECURSOR-Z + PPI; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX-8331|complex.ecocyc.CPLX-8331]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PRECURSOR-Z|molecule.ecocyc.PRECURSOR-Z]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C21310|molecule.C21310]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17809`

## Notes

CPD-19179 -> PRECURSOR-Z + PPI; direction=LEFT-TO-RIGHT
