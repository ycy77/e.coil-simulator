---
entity_id: "protein.P77455"
entity_type: "protein"
name: "paaZ"
source_database: "UniProt"
source_id: "P77455"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaZ maoC ydbN b1387 JW1382"
---

# paaZ

`protein.P77455`

## Static

- Type: `protein`
- Source: `UniProt:P77455`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolytic ring cleavage of 2-oxepin-2(3H)-ylideneacetyl-CoA (oxepin-CoA) via the open-chain aldehyde intermediate to yield 3-oxo-5,6-dehydrosuberyl-CoA. The enzyme consists of a C-terminal (R)-specific enoyl-CoA hydratase domain (formerly MaoC) that cleaves the ring and produces the highly reactive 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde and an N-terminal NADP-dependent aldehyde dehydrogenase domain that oxidizes the aldehyde to 3-oxo-5,6-dehydrosuberyl-CoA. Can also use crotonyl-CoA as substrate. {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:21296885, ECO:0000269|PubMed:9748275}.

## Biological Role

Catalyzes 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde:NADP+ oxidoreductase (reaction.R09820). Component of oxepin-CoA hydrolase [multifunctional] (complex.ecocyc.CPLX0-8538).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolytic ring cleavage of 2-oxepin-2(3H)-ylideneacetyl-CoA (oxepin-CoA) via the open-chain aldehyde intermediate to yield 3-oxo-5,6-dehydrosuberyl-CoA. The enzyme consists of a C-terminal (R)-specific enoyl-CoA hydratase domain (formerly MaoC) that cleaves the ring and produces the highly reactive 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde and an N-terminal NADP-dependent aldehyde dehydrogenase domain that oxidizes the aldehyde to 3-oxo-5,6-dehydrosuberyl-CoA. Can also use crotonyl-CoA as substrate. {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:21296885, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R09820|reaction.R09820]] `KEGG` `database` - via EC:1.2.1.91
- `is_component_of` --> [[complex.ecocyc.CPLX0-8538|complex.ecocyc.CPLX0-8538]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1387|gene.b1387]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77455`
- `KEGG:ecj:JW1382;eco:b1387;ecoc:C3026_08100;`
- `GeneID:945954;`
- `GO:GO:0004300; GO:0010124; GO:0016491; GO:0016620; GO:0016726; GO:0016803; GO:0016823; GO:0042802`
- `EC:1.2.1.91; 3.3.2.12`

## Notes

Bifunctional protein PaaZ [Includes: 2-oxepin-2(3H)-ylideneacetyl-CoA hydrolase (EC 3.3.2.12) (Oxepin-CoA hydrolase); 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase (EC 1.2.1.91)]
