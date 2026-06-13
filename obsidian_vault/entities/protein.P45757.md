---
entity_id: "protein.P45757"
entity_type: "protein"
name: "gspC"
source_database: "UniProt"
source_id: "P45757"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspC yheE b3324 JW3286"
---

# gspC

`protein.P45757`

## Static

- Type: `protein`
- Source: `UniProt:P45757`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of proteins. {ECO:0000305}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . GspC is predicted to be a bitopic inner membrane protein . gspC encodes the inner membrane platform protein of gram-negative type II secretion systems (see ). gsp: general secretory pathway (and see )

## Biological Role

Component of type II secretion system (complex.ecocyc.CPLX0-3382).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of proteins. {ECO:0000305}.

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3382|complex.ecocyc.CPLX0-3382]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3324|gene.b3324]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45757`
- `KEGG:ecj:JW3286;eco:b3324;ecoc:C3026_18060;`
- `GeneID:947824;`
- `GO:GO:0005886; GO:0015627; GO:0015628`

## Notes

Putative type II secretion system protein C (T2SS protein C) (Putative general secretion pathway protein C)
