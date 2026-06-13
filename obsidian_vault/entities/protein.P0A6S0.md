---
entity_id: "protein.P0A6S0"
entity_type: "protein"
name: "flgH"
source_database: "UniProt"
source_id: "P0A6S0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000250}; Lipid-anchor {ECO:0000250}. Bacterial flagellum basal body {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "flgH fla FVIII flaY b1079 JW5153"
---

# flgH

`protein.P0A6S0`

## Static

- Type: `protein`
- Source: `UniProt:P0A6S0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000250}; Lipid-anchor {ECO:0000250}. Bacterial flagellum basal body {ECO:0000250}.

## Enriched Summary

FUNCTION: Assembles around the rod to form the L-ring and probably protects the motor/basal body from shearing forces during rotation. {ECO:0000250}. FlgH is the basic subunit which makes up the L or lipopolysaccharide ring of the flagellar basal body. The L ring lies in the plane of the outer membrane and encircles the basal body rod . FlgH is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). Early studies in E. coli K-12 identified the flaY gene within the region I fla (flagella) genes (see ). Incomplete flagella structures are detected in mutants with defects in flaY . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Assembles around the rod to form the L-ring and probably protects the motor/basal body from shearing forces during rotation. {ECO:0000250}.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1079|gene.b1079]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6S0`
- `KEGG:ecj:JW5153;eco:b1079;ecoc:C3026_06540;`
- `GeneID:93776328;946996;`
- `GO:GO:0003774; GO:0006970; GO:0009279; GO:0009427; GO:0071973`

## Notes

Flagellar L-ring protein (Basal body L-ring protein)
