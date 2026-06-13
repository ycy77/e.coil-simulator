---
entity_id: "protein.P45762"
entity_type: "protein"
name: "gspK"
source_database: "UniProt"
source_id: "P45762"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:Q00518}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspK yheJ b3332 JW3294"
---

# gspK

`protein.P45762`

## Static

- Type: `protein`
- Source: `UniProt:P45762`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:Q00518}.

## Enriched Summary

FUNCTION: Component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Plays a role in pseudopilus assembly and seems to control its length. Interacts with the pseudopilus tip complex that is critical for the recognition and binding of secretion substrates. {ECO:0000250|UniProtKB:Q00518}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspK encodes a minor pseudopilin of gram-negative type II secretion systems (see ). GspK is predicted to be a bitopic inner membrane protein . gsp: general secretory pathway

## Biological Role

Component of type II secretion system (complex.ecocyc.CPLX0-3382).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Plays a role in pseudopilus assembly and seems to control its length. Interacts with the pseudopilus tip complex that is critical for the recognition and binding of secretion substrates. {ECO:0000250|UniProtKB:Q00518}.

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3382|complex.ecocyc.CPLX0-3382]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3332|gene.b3332]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45762`
- `KEGG:ecj:JW3294;eco:b3332;ecoc:C3026_18100;`
- `GeneID:947831;`
- `GO:GO:0005886; GO:0009306`

## Notes

Putative type II secretion system protein K (T2SS protein K) (Putative general secretion pathway protein K)
