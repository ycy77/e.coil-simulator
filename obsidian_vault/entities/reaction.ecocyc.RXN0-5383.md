---
entity_id: "reaction.ecocyc.RXN0-5383"
entity_type: "reaction"
name: "RXN0-5383"
source_database: "EcoCyc"
source_id: "RXN0-5383"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5383

`reaction.ecocyc.RXN0-5383`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5383`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-21359 + UNDECAPRENYL-DIPHOSPHATE -> CPD0-1151 + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21359 + UNDECAPRENYL-DIPHOSPHATE -> CPD0-1151 + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lpxT (protein.P76445). Substrates: di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359). Products: di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556), lipid A-core 1-diphosphate (molecule.ecocyc.CPD0-1151).

## Annotation

CPD-21359 + UNDECAPRENYL-DIPHOSPHATE -> CPD0-1151 + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P76445|protein.P76445]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1151|molecule.ecocyc.CPD0-1151]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[protein.G3MTW7|protein.G3MTW7]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5383`

## Notes

CPD-21359 + UNDECAPRENYL-DIPHOSPHATE -> CPD0-1151 + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT
