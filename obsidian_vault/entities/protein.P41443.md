---
entity_id: "protein.P41443"
entity_type: "protein"
name: "gspH"
source_database: "UniProt"
source_id: "P41443"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:Q00515}; Single-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspH hofH hopH b3329 JW3291"
---

# gspH

`protein.P41443`

## Static

- Type: `protein`
- Source: `UniProt:P41443`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:Q00515}; Single-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Part of the pseudopilus tip complex that is critical for the recognition and binding of secretion substrates. {ECO:0000250|UniProtKB:Q00515}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspH encodes a minor pseudopilin of gram-negative type II secretion systems (see ). gsp: general secretory pathway hopH: homology with PulH (see )

## Biological Role

Component of type II secretion system (complex.ecocyc.CPLX0-3382).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Part of the pseudopilus tip complex that is critical for the recognition and binding of secretion substrates. {ECO:0000250|UniProtKB:Q00515}.

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3382|complex.ecocyc.CPLX0-3382]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3329|gene.b3329]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P41443`
- `KEGG:ecj:JW3291;eco:b3329;ecoc:C3026_18085;`
- `GeneID:947834;`
- `GO:GO:0005886; GO:0015627; GO:0015628`

## Notes

Type II secretion system protein H (T2SS minor pseudopilin H) (General secretion pathway protein H) (Protein transport protein HofH) (Putative general secretion pathway protein H)
