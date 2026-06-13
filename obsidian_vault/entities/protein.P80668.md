---
entity_id: "protein.P80668"
entity_type: "protein"
name: "feaB"
source_database: "UniProt"
source_id: "P80668"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "feaB maoB padA ydbG b1385 JW1380"
---

# feaB

`protein.P80668`

## Static

- Type: `protein`
- Source: `UniProt:P80668`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts almost equally well on phenylacetaldehyde, 4-hydroxyphenylacetaldehyde and 3,4-dihydroxyphenylacetaldehyde.

## Biological Role

Component of phenylacetaldehyde dehydrogenase (complex.ecocyc.PHENDEHYD-CPLX).

## Enriched Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Acts almost equally well on phenylacetaldehyde, 4-hydroxyphenylacetaldehyde and 3,4-dihydroxyphenylacetaldehyde.

## Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PHENDEHYD-CPLX|complex.ecocyc.PHENDEHYD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1385|gene.b1385]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P80668`
- `KEGG:ecj:JW1380;eco:b1385;ecoc:C3026_08090;`
- `GeneID:75203471;945933;`
- `GO:GO:0006559; GO:0008957; GO:0009435; GO:0016491; GO:0019607; GO:0032991; GO:0046196; GO:0047106`
- `EC:1.2.1.39`

## Notes

Phenylacetaldehyde dehydrogenase (PAD) (EC 1.2.1.39)
