---
entity_id: "complex.ecocyc.CPLX-9493"
entity_type: "complex"
name: "CcmAB"
source_database: "EcoCyc"
source_id: "CPLX-9493"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# CcmAB

`complex.ecocyc.CPLX-9493`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-9493`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABL8|protein.P0ABL8]], [[protein.P33931|protein.P33931]]

## Enriched Summary

The cytochrome c maturation proteins A and B (CcmA and CcmB) are part of the multiprotein type I PWY-8147 "cytochrome c biogenesis system". CcmA and CcmB promote the release of holo(heme)-CcmE from CCMC-MONOMER "CcmC"; in the absence of CcmA or CcmB, holoCcmE remains bound to CcmC . CcmAB is present in the membrane fraction of cells and the purified complex has ATPase activity in vitro; CcmA contains the sequence features of ATP-binding proteins and is predicted to be a cytoplasmic protein; CcmB is predicted to be an integral membrane protein with 6 transmembrane regions . The cytochrome c maturation proteins A and B (CcmA and CcmB) are part of the multiprotein type I PWY-8147 "cytochrome c biogenesis system". CcmA and CcmB promote the release of holo(heme)-CcmE from CCMC-MONOMER "CcmC"; in the absence of CcmA or CcmB, holoCcmE remains bound to CcmC . CcmAB is present in the membrane fraction of cells and the purified complex has ATPase activity in vitro; CcmA contains the sequence features of ATP-binding proteins and is predicted to be a cytoplasmic protein; CcmB is predicted to be an integral membrane protein with 6 transmembrane regions .

## Biological Role

Catalyzes RXN-21408 (reaction.ecocyc.RXN-21408).

## Annotation

The cytochrome c maturation proteins A and B (CcmA and CcmB) are part of the multiprotein type I PWY-8147 "cytochrome c biogenesis system". CcmA and CcmB promote the release of holo(heme)-CcmE from CCMC-MONOMER "CcmC"; in the absence of CcmA or CcmB, holoCcmE remains bound to CcmC . CcmAB is present in the membrane fraction of cells and the purified complex has ATPase activity in vitro; CcmA contains the sequence features of ATP-binding proteins and is predicted to be a cytoplasmic protein; CcmB is predicted to be an integral membrane protein with 6 transmembrane regions .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21408|reaction.ecocyc.RXN-21408]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0ABL8|protein.P0ABL8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P33931|protein.P33931]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX-9493`
- `PDB:7VFP`
- `PDB:7VFJ`
- `PDB:7F04`
- `PDB:7F03`
- `PDB:7F02`
- `QSPROTEOME:QS00274385`

## Notes

1*protein.P0ABL8|2*protein.P33931
