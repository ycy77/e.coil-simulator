---
entity_id: "protein.P06974"
entity_type: "protein"
name: "fliM"
source_database: "UniProt"
source_id: "P06974"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein. Bacterial flagellum basal body."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliM cheC2 fla AII fla QII b1945 JW1929"
---

# fliM

`protein.P06974`

## Static

- Type: `protein`
- Source: `UniProt:P06974`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein. Bacterial flagellum basal body.

## Enriched Summary

FUNCTION: FliM is one of three proteins (FliG, FliN, FliM) that forms the rotor-mounted switch complex (C ring), located at the base of the basal body. This complex interacts with the CheY and CheZ chemotaxis proteins, in addition to contacting components of the motor that determine the direction of flagellar rotation. FliM is one of three components of the flagellar motor's "switch complex." Expression of fliM is upregulated by ZnSO4 in the medium, and a fliM mutant is hypersensitive to ZnSO4 . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see cheC: see

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: FliM is one of three proteins (FliG, FliN, FliM) that forms the rotor-mounted switch complex (C ring), located at the base of the basal body. This complex interacts with the CheY and CheZ chemotaxis proteins, in addition to contacting components of the motor that determine the direction of flagellar rotation.

## Pathways

- `eco02030` Bacterial chemotaxis (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1945|gene.b1945]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06974`
- `KEGG:ecj:JW1929;eco:b1945;ecoc:C3026_11015;`
- `GeneID:946442;`
- `GO:GO:0003774; GO:0005886; GO:0006935; GO:0009288; GO:0009433; GO:0050918; GO:0071977; GO:0071978; GO:0120107`

## Notes

Flagellar motor switch protein FliM
