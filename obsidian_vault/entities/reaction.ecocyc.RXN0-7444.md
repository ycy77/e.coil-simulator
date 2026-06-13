---
entity_id: "reaction.ecocyc.RXN0-7444"
entity_type: "reaction"
name: "RXN0-7444"
source_database: "EcoCyc"
source_id: "RXN0-7444"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7444

`reaction.ecocyc.RXN0-7444`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7444`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The chromosomal locus datA and the replication machinery-associated G7313-MONOMER "Hda protein" both reduce the potential of replication initiation by promoting the hydrolysis of DnaA-ATP (the active form of DnaA in replication initiation) to DnaA-ADP . EcoCyc reaction equation: MONOMER0-160 + WATER -> MONOMER0-4565 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. The chromosomal locus datA and the replication machinery-associated G7313-MONOMER "Hda protein" both reduce the potential of replication initiation by promoting the hydrolysis of DnaA-ATP (the active form of DnaA in replication initiation) to DnaA-ADP .

## Biological Role

Catalyzed by Hda-β-clamp complex (complex.ecocyc.CPLX0-10342). Substrates: H2O (molecule.C00001). Products: phosphate (molecule.ecocyc.Pi).

## Annotation

The chromosomal locus datA and the replication machinery-associated G7313-MONOMER "Hda protein" both reduce the potential of replication initiation by promoting the hydrolysis of DnaA-ATP (the active form of DnaA in replication initiation) to DnaA-ADP .

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-10342|complex.ecocyc.CPLX0-10342]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7444`

## Notes

MONOMER0-160 + WATER -> MONOMER0-4565 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
