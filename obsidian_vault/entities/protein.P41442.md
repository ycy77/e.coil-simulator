---
entity_id: "protein.P41442"
entity_type: "protein"
name: "gspG"
source_database: "UniProt"
source_id: "P41442"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:Q00514}; Single-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspG hofG hopG b3328 JW3290"
---

# gspG

`protein.P41442`

## Static

- Type: `protein`
- Source: `UniProt:P41442`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:Q00514}; Single-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Core component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Pseudopilin (pilin-like) protein that polymerizes to form the pseudopilus. Further polymerization triggers pseudopilus growth. {ECO:0000250|UniProtKB:Q00514}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . GspG is predicted to be a bitopic inner membrane protein . gspG encodes the major pseudopilin of gram-negative type II secretion systems (see ). gspG was significantly upregulated in simulated microgravity . gsp: general secretory pathway hopG: homology with PulG, OutG and ExeG (see )

## Biological Role

Component of type II secretion system (complex.ecocyc.CPLX0-3382).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Core component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Pseudopilin (pilin-like) protein that polymerizes to form the pseudopilus. Further polymerization triggers pseudopilus growth. {ECO:0000250|UniProtKB:Q00514}.

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3382|complex.ecocyc.CPLX0-3382]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3328|gene.b3328]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P41442`
- `KEGG:ecj:JW3290;eco:b3328;ecoc:C3026_18080;`
- `GeneID:947827;`
- `GO:GO:0005886; GO:0015627; GO:0015628`

## Notes

Type II secretion system core protein G (T2SS core protein G) (Protein transport protein HofG) (Putative general secretion pathway protein G)
