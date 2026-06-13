---
entity_id: "protein.P0ABZ1"
entity_type: "protein"
name: "fliG"
source_database: "UniProt"
source_id: "P0ABZ1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Cytoplasmic side. Bacterial flagellum basal body."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliG fla AII.2 fla BII b1939 JW1923"
---

# fliG

`protein.P0ABZ1`

## Static

- Type: `protein`
- Source: `UniProt:P0ABZ1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein; Cytoplasmic side. Bacterial flagellum basal body.

## Enriched Summary

FUNCTION: FliG is one of three proteins (FliG, FliN, FliM) that forms the rotor-mounted switch complex (C ring), located at the base of the basal body. This complex interacts with the CheY and CheZ chemotaxis proteins, in addition to contacting components of the motor that determine the direction of flagellar rotation. FliG is one of three components of the flagellar motor's "switch complex." FliG proteins consist of N-terminal (N), middle (M) and C-terminal (C) domains separated by short flexible linkers (helixNM and helixMC); the M and C domains each contain an Armadillo-repeat motif (ARMM and ARMC). FliG is monomeric in solution but forms a multimeric ring structure during assembly of the flagellar complex; FliG monomers are linked together by intermolecular ARMM-ARMC interactions; the FliG ring assembles using a domain-swap polymerization mechanism (see ). For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: FliG is one of three proteins (FliG, FliN, FliM) that forms the rotor-mounted switch complex (C ring), located at the base of the basal body. This complex interacts with the CheY and CheZ chemotaxis proteins, in addition to contacting components of the motor that determine the direction of flagellar rotation.

## Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1939|gene.b1939]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABZ1`
- `KEGG:ecj:JW1923;eco:b1939;ecoc:C3026_10985;`
- `GeneID:75172058;75205820;946451;`
- `GO:GO:0003774; GO:0005886; GO:0006935; GO:0009288; GO:0009433; GO:0042802; GO:0044780; GO:0071973; GO:0071977; GO:0120107`

## Notes

Flagellar motor switch protein FliG
