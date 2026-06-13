---
entity_id: "protein.P45758"
entity_type: "protein"
name: "gspD"
source_database: "UniProt"
source_id: "P45758"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:28067918}. Note=Most of the protein is in the periplasm which it traverses to contact proteins of the cell inner membrane. {ECO:0000305|PubMed:28067918}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspD yheF b3325 JW5707"
---

# gspD

`protein.P45758`

## Static

- Type: `protein`
- Source: `UniProt:P45758`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:28067918}. Note=Most of the protein is in the periplasm which it traverses to contact proteins of the cell inner membrane. {ECO:0000305|PubMed:28067918}.

## Enriched Summary

FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of folded proteins across the outer membrane. This subunit would form the outer membrane channel. {ECO:0000250|UniProtKB:E3PJ86}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspD encodes the outer membrane channel or 'secretin' of gram-negative type II secretion systems (see ). Purified GspD adopts a pentadecameric structure forming a cylindrical channel; the K-12 GspD protomer consists of five domains: 3 N domains (N1, N2, N3) which form the periplasmic chamber plus the secretin and S domain which form the pore structure in the OM . gspD in E. coli K-12 encodes a Klebsiella-type GspDα secretin; cryo-ET in-situ structures of GspDα on the inner and outer membrane have been obtained and a model of secretin translocation proposed . gsp: general secretory pathway

## Biological Role

Component of type II secretion system (complex.ecocyc.CPLX0-3382).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of folded proteins across the outer membrane. This subunit would form the outer membrane channel. {ECO:0000250|UniProtKB:E3PJ86}.

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3382|complex.ecocyc.CPLX0-3382]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3325|gene.b3325]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45758`
- `KEGG:ecj:JW5707;eco:b3325;ecoc:C3026_18065;`
- `GeneID:947822;`
- `GO:GO:0009279; GO:0009306; GO:0015627; GO:0015628; GO:0042802`

## Notes

Putative secretin GspD (Putative general secretion pathway protein D) (Putative type II secretion system protein D) (T2SS protein D)
