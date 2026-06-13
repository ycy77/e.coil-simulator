---
entity_id: "protein.P77747"
entity_type: "protein"
name: "ompN"
source_database: "UniProt"
source_id: "P77747"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ompN ynaG b1377 JW1371"
---

# ompN

`protein.P77747`

## Static

- Type: `protein`
- Source: `UniProt:P77747`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Forms pores that allow passive diffusion of small molecules across the outer membrane (By similarity). Non-specific porin. {ECO:0000250}. Though under typical laboratory growth conditions OmpN is not highly expressed, when overexpressed it operates as a porin with single-channel conductance properties similar to those of OmpC . OmpN abundance is regulated by TKE8-RNA. ompN exhibits mosaic evolution patterns in E. coli .

## Biological Role

Catalyzes RXN0-2481 (reaction.ecocyc.RXN0-2481).

## Annotation

FUNCTION: Forms pores that allow passive diffusion of small molecules across the outer membrane (By similarity). Non-specific porin. {ECO:0000250}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2481|reaction.ecocyc.RXN0-2481]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1377|gene.b1377]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77747`
- `KEGG:ecj:JW1371;eco:b1377;ecoc:C3026_08045;`
- `GeneID:946313;`
- `GO:GO:0009279; GO:0015288; GO:0016020; GO:0034219; GO:0034220; GO:0046930`

## Notes

Outer membrane porin N (Outer membrane protein N) (Porin OmpN)
