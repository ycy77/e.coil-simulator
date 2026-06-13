---
entity_id: "protein.P39832"
entity_type: "protein"
name: "znuB"
source_database: "UniProt"
source_id: "P39832"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "znuB yebI b1859 JW1848"
---

# znuB

`protein.P39832`

## Static

- Type: `protein`
- Source: `UniProt:P39832`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in the high-affinity zinc uptake transport system. znuB encodes the predicted integral membrane subunit of an ATP-dependent Zn2+ uptake system znu: Zn2+ uptake

## Biological Role

Component of Zn2+ ABC transporter (complex.ecocyc.ABC-63-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Involved in the high-affinity zinc uptake transport system.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-63-CPLX|complex.ecocyc.ABC-63-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1859|gene.b1859]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39832`
- `KEGG:ecj:JW1848;eco:b1859;ecoc:C3026_10590;`
- `GeneID:946372;`
- `GO:GO:0000006; GO:0005886; GO:0010043; GO:0016020; GO:0055052; GO:0071578`

## Notes

High-affinity zinc uptake system membrane protein ZnuB
