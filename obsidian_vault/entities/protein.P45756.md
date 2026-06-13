---
entity_id: "protein.P45756"
entity_type: "protein"
name: "gspA"
source_database: "UniProt"
source_id: "P45756"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspA yheD b3323 JW3285"
---

# gspA

`protein.P45756`

## Static

- Type: `protein`
- Source: `UniProt:P45756`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: May play a regulatory role under conditions of derepressed gsp gene expression. {ECO:0000269|PubMed:11118204}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system (T2SS); the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . GspA is predicted to be a bitopic inner membrane protein . The inner membrane proteins GspA and GspB contribute to G7703-MONOMER secretin assembly and transport in some gram-negative T2SSs (see ). gsp: general secretory pathway (and see )

## Annotation

FUNCTION: May play a regulatory role under conditions of derepressed gsp gene expression. {ECO:0000269|PubMed:11118204}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3323|gene.b3323]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45756`
- `KEGG:ecj:JW3285;eco:b3323;ecoc:C3026_18055;`
- `GeneID:947825;`
- `GO:GO:0005524; GO:0005829; GO:0005886; GO:0016887`

## Notes

Putative general secretion pathway protein A
