---
entity_id: "protein.P41441"
entity_type: "protein"
name: "gspF"
source_database: "UniProt"
source_id: "P41441"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspF hofF hopF b3327 JW3289"
---

# gspF

`protein.P41441`

## Static

- Type: `protein`
- Source: `UniProt:P41441`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Component of the type II secretion system inner membrane complex required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. {ECO:0000250|UniProtKB:Q00514}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspF encodes a component of the inner membrane platform of gram-negative type II secretion systems (see ). gsp: general secretory pathway hopF: homology with PulF (see )

## Biological Role

Component of type II secretion system (complex.ecocyc.CPLX0-3382).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Component of the type II secretion system inner membrane complex required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. {ECO:0000250|UniProtKB:Q00514}.

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3382|complex.ecocyc.CPLX0-3382]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3327|gene.b3327]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P41441`
- `KEGG:ecj:JW3289;eco:b3327;ecoc:C3026_18075;`
- `GeneID:947829;`
- `GO:GO:0005886; GO:0015627; GO:0015628; GO:0046872`

## Notes

Putative type II secretion system protein F (T2SS protein F) (General secretion pathway protein F) (Protein transport protein HofF)
