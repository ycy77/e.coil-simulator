---
entity_id: "protein.P03825"
entity_type: "protein"
name: "gspB"
source_database: "UniProt"
source_id: "P03825"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspB pinO pioO pno b3322 JW3284"
---

# gspB

`protein.P03825`

## Static

- Type: `protein`
- Source: `UniProt:P03825`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of a cryptic operon that encodes proteins involved in type II secretion pathway in other organisms, but is not expressed in strain K12 under standard laboratory conditions (PubMed:8655552). May play a regulatory role under conditions of derepressed gsp gene expression (PubMed:11118204). {ECO:0000269|PubMed:11118204, ECO:0000305|PubMed:8655552}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system (T2SS); the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . The inner membrane proteins GspA and GspB contribute to G7703-MONOMER secretin assembly and transport in some gram-negative T2SSs (see ). Comment from EcoGene: gspB was initially identified as an ORF that might be the 11.3 kDa "initiation protein" PinO synthesized in the absence of isoleucine in relA stains (). But GspB is predicted to be 15.9 kDa and has isoleucine residues and there is no evidence that gspB encodes the PinO peptide or that it binds calcium. No homology to calmodulin or other calcium-binding proteins is predicted...

## Annotation

FUNCTION: Part of a cryptic operon that encodes proteins involved in type II secretion pathway in other organisms, but is not expressed in strain K12 under standard laboratory conditions (PubMed:8655552). May play a regulatory role under conditions of derepressed gsp gene expression (PubMed:11118204). {ECO:0000269|PubMed:11118204, ECO:0000305|PubMed:8655552}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3322|gene.b3322]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03825`
- `KEGG:ecj:JW3284;eco:b3322;ecoc:C3026_18050;`
- `GeneID:947826;`
- `GO:GO:0005886`

## Notes

Putative general secretion pathway protein B
