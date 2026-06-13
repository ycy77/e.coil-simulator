---
entity_id: "protein.P04949"
entity_type: "protein"
name: "fliC"
source_database: "UniProt"
source_id: "P04949"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Secreted. Bacterial flagellum."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliC flaF hag b1923 JW1908"
---

# fliC

`protein.P04949`

## Static

- Type: `protein`
- Source: `UniProt:P04949`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Secreted. Bacterial flagellum.

## Enriched Summary

FUNCTION: Flagellin is the subunit protein which polymerizes to form the filaments of bacterial flagella. FliC, or flagellin, is the basic subunit that polymerizes to form the rigid flagellar filament of Escherichia coli. fliC was found upregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see . The 'pole-localizer' protein G7087-MONOMER TmaR protects and stabilizes fliA transcripts .

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Flagellin is the subunit protein which polymerizes to form the filaments of bacterial flagella.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1923|gene.b1923]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04949`
- `KEGG:ecj:JW1908;eco:b1923;`
- `GeneID:949101;`
- `GO:GO:0005198; GO:0005576; GO:0009288; GO:0071973`

## Notes

Flagellin
