---
entity_id: "protein.P0A6S3"
entity_type: "protein"
name: "flgI"
source_database: "UniProt"
source_id: "P0A6S3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm. Bacterial flagellum basal body."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "flgI fla FIX flaM b1080 JW1067"
---

# flgI

`protein.P0A6S3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6S3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm. Bacterial flagellum basal body.

## Enriched Summary

FUNCTION: Assembles around the rod to form the L-ring and probably protects the motor/basal body from shearing forces during rotation. FlgI is the structural component of the P (peptidoglycan ring) of the flagellar basal body . FlgI and FlgH (the structural component of the L ring) form the L-P ring complex which assembles around the rod and is thought to act as the molecular bushing that supports flagellar motor rotation (see ). Our knowledge on FlgI in E. coli is based, in part, on characterization of the homologous protein in Salmonella typhimurium (see ); the two proteins are 92% identical over their entire length. E. coli FlgI contains an intramolecular disulfide bond; the presence of this bond does not appear to be necessary for P-ring formation but has been implicated in preventing degradation of the protein in the periplasmic space . Cross-linking experiments suggest that FlgI may interact with the stator protein MotB . Early studies in E. coli K-12 identified the flaM gene within the region I fla (flagella) genes (see ). Incomplete flagella structures are detected in mutants with defects in flaM . flaM mutants are non-motile (see also ). For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Assembles around the rod to form the L-ring and probably protects the motor/basal body from shearing forces during rotation.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1080|gene.b1080]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6S3`
- `KEGG:ecj:JW1067;eco:b1080;ecoc:C3026_06545;`
- `GeneID:75171205;75203667;947534;`
- `GO:GO:0005198; GO:0006974; GO:0009428; GO:0030288; GO:0071973`

## Notes

Flagellar P-ring protein (Basal body P-ring protein)
