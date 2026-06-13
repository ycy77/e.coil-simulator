---
entity_id: "protein.P39829"
entity_type: "protein"
name: "garD"
source_database: "UniProt"
source_id: "P39829"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "garD yhaG b3128 JW3097"
---

# garD

`protein.P39829`

## Static

- Type: `protein`
- Source: `UniProt:P39829`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of galactarate to form 5-dehydro-4-deoxy-D-glucarate (5-KDG). {ECO:0000255|HAMAP-Rule:MF_02031, ECO:0000269|PubMed:31811683, ECO:0000269|PubMed:9772162}.

## Biological Role

Component of galactarate dehydratase (complex.ecocyc.CPLX0-8537).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of galactarate to form 5-dehydro-4-deoxy-D-glucarate (5-KDG). {ECO:0000255|HAMAP-Rule:MF_02031, ECO:0000269|PubMed:31811683, ECO:0000269|PubMed:9772162}.

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8537|complex.ecocyc.CPLX0-8537]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3128|gene.b3128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39829`
- `KEGG:ecj:JW3097;eco:b3128;ecoc:C3026_17050;`
- `GeneID:947641;`
- `GO:GO:0008198; GO:0008867; GO:0019698; GO:0042803; GO:0046392`
- `EC:4.2.1.42`

## Notes

Galactarate dehydratase (L-threo-forming) (GalcD) (EC 4.2.1.42)
