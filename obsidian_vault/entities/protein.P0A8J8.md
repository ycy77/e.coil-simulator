---
entity_id: "protein.P0A8J8"
entity_type: "protein"
name: "rhlB"
source_database: "UniProt"
source_id: "P0A8J8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00661, ECO:0000269|PubMed:18337249}. Note=Forms a cytoskeletal-like coiled structure that extends along the length of the cell. Formation of this structure does not require the presence of RNase E, MinD and/or MreB."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhlB mmrA b3780 JW3753"
---

# rhlB

`protein.P0A8J8`

## Static

- Type: `protein`
- Source: `UniProt:P0A8J8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00661, ECO:0000269|PubMed:18337249}. Note=Forms a cytoskeletal-like coiled structure that extends along the length of the cell. Formation of this structure does not require the presence of RNase E, MinD and/or MreB.

## Enriched Summary

FUNCTION: DEAD-box RNA helicase involved in RNA degradation. Has RNA-dependent ATPase activity and unwinds double-stranded RNA. {ECO:0000255|HAMAP-Rule:MF_00661, ECO:0000269|PubMed:12181321, ECO:0000269|PubMed:8610017, ECO:0000269|PubMed:9732274}.

## Biological Role

Component of degradosome (complex.ecocyc.CPLX0-2381), ATP-dependent RNA helicase RhlB (complex.ecocyc.CPLX0-3541).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: DEAD-box RNA helicase involved in RNA degradation. Has RNA-dependent ATPase activity and unwinds double-stranded RNA. {ECO:0000255|HAMAP-Rule:MF_00661, ECO:0000269|PubMed:12181321, ECO:0000269|PubMed:8610017, ECO:0000269|PubMed:9732274}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3541|complex.ecocyc.CPLX0-3541]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3780|gene.b3780]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8J8`
- `KEGG:ecj:JW3753;eco:b3780;ecoc:C3026_20465;`
- `GeneID:93778164;948290;`
- `GO:GO:0003723; GO:0003724; GO:0005524; GO:0005829; GO:0006396; GO:0006401; GO:0016020; GO:0016887; GO:0042803; GO:0097718; GO:1990061`
- `EC:3.6.4.13`

## Notes

ATP-dependent RNA helicase RhlB (EC 3.6.4.13)
