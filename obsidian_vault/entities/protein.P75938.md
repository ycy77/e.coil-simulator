---
entity_id: "protein.P75938"
entity_type: "protein"
name: "flgF"
source_database: "UniProt"
source_id: "P75938"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial flagellum basal body."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "flgF fla FVI flaX b1077 JW1064"
---

# flgF

`protein.P75938`

## Static

- Type: `protein`
- Source: `UniProt:P75938`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial flagellum basal body.

## Enriched Summary

Flagellar basal-body rod protein FlgF (Putative proximal rod protein) FlgF is one of four proteins that comprise the rod of the flagellar basal body. FlgF is best characterized in Salmonella Typhimurium (see ); flagella structure, assembly and motor function are considered to be widely the same in Salmonella Typhimurium and E. coli. The FlgF proteins from these two species share 87% sequence identity. Early studies in E. coli K-12 identified the flaX gene within the region I fla (flagella) genes (see ). K-12 flaX mutants lack detectable flagellar structures when examined by electron microscscopy . flgF mutants ('Ec:flgFi') are non-motile . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

Flagellar basal-body rod protein FlgF (Putative proximal rod protein)

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1077|gene.b1077]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75938`
- `KEGG:ecj:JW1064;eco:b1077;ecoc:C3026_06530;`
- `GeneID:945639;`
- `GO:GO:0006935; GO:0009288; GO:0030694; GO:0071973; GO:0071978`

## Notes

Flagellar basal-body rod protein FlgF (Putative proximal rod protein)
