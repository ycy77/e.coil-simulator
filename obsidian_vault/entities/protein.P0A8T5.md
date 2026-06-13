---
entity_id: "protein.P0A8T5"
entity_type: "protein"
name: "fliE"
source_database: "UniProt"
source_id: "P0A8T5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial flagellum basal body {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliE fla AI flaN b1937 JW1921"
---

# fliE

`protein.P0A8T5`

## Static

- Type: `protein`
- Source: `UniProt:P0A8T5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial flagellum basal body {ECO:0000250}.

## Enriched Summary

Flagellar hook-basal body complex protein FliE fliE is predicted to encode a structural protein of the flagellum hook-basal body complex. fliE constitutes a monocistronic operon in both E. coli K-12 and Salmonella typhimurium and the proteins are 82% identical (see also ). In Salmonella typhimurium, FliE is a component of the hook-basal body complex; it may act as a structural adaptor between the MS ring and the rod . Insertional inactivation of fliE in Salmonella typhimurium results in mutants that are unable to secrete flagellin (FliC) or assemble flagella . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see .

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452), flagellar basal body (complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

Flagellar hook-basal body complex protein FliE

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX|complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1937|gene.b1937]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8T5`
- `KEGG:ecj:JW1921;eco:b1937;ecoc:C3026_10975;`
- `GeneID:93775248;946446;`
- `GO:GO:0003774; GO:0005198; GO:0006935; GO:0009288; GO:0009425; GO:0030694; GO:0044780; GO:0071973`

## Notes

Flagellar hook-basal body complex protein FliE
