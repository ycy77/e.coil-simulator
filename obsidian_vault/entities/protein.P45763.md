---
entity_id: "protein.P45763"
entity_type: "protein"
name: "gspL"
source_database: "UniProt"
source_id: "P45763"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P25060}; Single-pass membrane protein {ECO:0000250|UniProtKB:P25060}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspL yheK b3333 JW5705"
---

# gspL

`protein.P45763`

## Static

- Type: `protein`
- Source: `UniProt:P45763`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P25060}; Single-pass membrane protein {ECO:0000250|UniProtKB:P25060}.

## Enriched Summary

FUNCTION: Inner membrane component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Plays a role in the complex assembly and recruits GspM resulting in a stable complex in the inner membrane. Provides thus a link between the energy-providing GspE protein in the cytoplasm and the rest of the T2SS machinery. {ECO:0000250|UniProtKB:P25060}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspL encodes a component of the inner membrane platform of gram-negative type II secretion systems (see ). gsp: general secretory pathway

## Biological Role

Component of type II secretion system (complex.ecocyc.CPLX0-3382).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Inner membrane component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Plays a role in the complex assembly and recruits GspM resulting in a stable complex in the inner membrane. Provides thus a link between the energy-providing GspE protein in the cytoplasm and the rest of the T2SS machinery. {ECO:0000250|UniProtKB:P25060}.

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3382|complex.ecocyc.CPLX0-3382]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3333|gene.b3333]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45763`
- `KEGG:ecj:JW5705;eco:b3333;ecoc:C3026_18105;`
- `GeneID:947842;`
- `GO:GO:0005886; GO:0009276; GO:0015627; GO:0015628`

## Notes

Putative type II secretion system protein L (T2SS protein L) (Putative general secretion pathway protein L)
