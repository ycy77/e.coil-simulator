---
entity_id: "protein.P0ABW9"
entity_type: "protein"
name: "flgB"
source_database: "UniProt"
source_id: "P0ABW9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial flagellum basal body {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "flgB fla FII flbA b1073 JW1060"
---

# flgB

`protein.P0ABW9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABW9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial flagellum basal body {ECO:0000250}.

## Enriched Summary

FUNCTION: Structural component of flagellum, the bacterial motility apparatus. Part of the rod structure of flagellar basal body (By similarity). {ECO:0000250}. FlgB is one of four proteins that comprise the rod of the flagellar basal body. FlgB is best characterized in Salmonella Typhimurium (see ); flagella structure, assembly and motor function are considered to be widely the same in Salmonella Typhimurium and E. coli. The FlgB proteins from these two species share 81% sequence identity. Early studies in E. coli K-12 identified the flbA gene within the region I fla (flagella) genes (see ). K-12 flbA mutants lack detectable flagellar structures when examined by electron microscscopy . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Structural component of flagellum, the bacterial motility apparatus. Part of the rod structure of flagellar basal body (By similarity). {ECO:0000250}.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1073|gene.b1073]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABW9`
- `KEGG:ecj:JW1060;eco:b1073;ecoc:C3026_06510;`
- `GeneID:93776334;945678;`
- `GO:GO:0006935; GO:0009288; GO:0030694; GO:0071973`

## Notes

Flagellar basal body rod protein FlgB (Putative proximal rod protein)
