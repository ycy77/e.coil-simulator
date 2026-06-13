---
entity_id: "protein.P0AC92"
entity_type: "protein"
name: "gnsA"
source_database: "UniProt"
source_id: "P0AC92"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gnsA yccL b4517 JW0976"
---

# gnsA

`protein.P0AC92`

## Static

- Type: `protein`
- Source: `UniProt:P0AC92`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Overexpression increases levels of unsaturated fatty acids and suppresses both the temperature-sensitive fabA6 mutation and cold-sensitive secG null mutation. {ECO:0000269|PubMed:11544213}.

## Biological Role

Component of putative phosphatidylethanolamine synthesis regulator GnsA (complex.ecocyc.CPLX0-8177).

## Annotation

FUNCTION: Overexpression increases levels of unsaturated fatty acids and suppresses both the temperature-sensitive fabA6 mutation and cold-sensitive secG null mutation. {ECO:0000269|PubMed:11544213}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8177|complex.ecocyc.CPLX0-8177]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4517|gene.b4517]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC92`
- `KEGG:ecj:JW0976;eco:b4517;ecoc:C3026_06045;`
- `GeneID:1450249;93776419;`
- `GO:GO:0005829; GO:0006646; GO:0042802; GO:0042803; GO:2001279`

## Notes

Protein GnsA
