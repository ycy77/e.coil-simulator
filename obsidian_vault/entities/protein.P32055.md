---
entity_id: "protein.P32055"
entity_type: "protein"
name: "fcl"
source_database: "UniProt"
source_id: "P32055"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fcl wcaG yefB b2052 JW2037"
---

# fcl

`protein.P32055`

## Static

- Type: `protein`
- Source: `UniProt:P32055`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the two-step NADP-dependent conversion of GDP-4-dehydro-6-deoxy-D-mannose to GDP-fucose, involving an epimerase and a reductase reaction. {ECO:0000255|HAMAP-Rule:MF_00956, ECO:0000269|PubMed:10480878, ECO:0000269|PubMed:11021971, ECO:0000269|PubMed:9473059}.

## Biological Role

Component of GDP-L-fucose synthase (complex.ecocyc.CPLX0-3881).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the two-step NADP-dependent conversion of GDP-4-dehydro-6-deoxy-D-mannose to GDP-fucose, involving an epimerase and a reductase reaction. {ECO:0000255|HAMAP-Rule:MF_00956, ECO:0000269|PubMed:10480878, ECO:0000269|PubMed:11021971, ECO:0000269|PubMed:9473059}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3881|complex.ecocyc.CPLX0-3881]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2052|gene.b2052]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32055`
- `KEGG:ecj:JW2037;eco:b2052;ecoc:C3026_11550;`
- `GeneID:946563;`
- `GO:GO:0005737; GO:0009242; GO:0016853; GO:0042351; GO:0042803; GO:0050577; GO:0070401`
- `EC:1.1.1.271`

## Notes

GDP-L-fucose synthase (EC 1.1.1.271) (GDP-4-keto-6-deoxy-D-mannose-3,5-epimerase-4-reductase)
