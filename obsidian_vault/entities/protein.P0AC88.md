---
entity_id: "protein.P0AC88"
entity_type: "protein"
name: "gmd"
source_database: "UniProt"
source_id: "P0AC88"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gmd yefA yefN b2053 JW2038"
---

# gmd

`protein.P0AC88`

## Static

- Type: `protein`
- Source: `UniProt:P0AC88`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of GDP-D-mannose to GDP-4-dehydro-6-deoxy-D-mannose. {ECO:0000255|HAMAP-Rule:MF_00955, ECO:0000269|PubMed:9257704}.

## Biological Role

Component of GDP-mannose 4,6-dehydratase (complex.ecocyc.GDPMANDEHYDRA-CPLX).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of GDP-D-mannose to GDP-4-dehydro-6-deoxy-D-mannose. {ECO:0000255|HAMAP-Rule:MF_00955, ECO:0000269|PubMed:9257704}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GDPMANDEHYDRA-CPLX|complex.ecocyc.GDPMANDEHYDRA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2053|gene.b2053]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC88`
- `KEGG:ecj:JW2038;eco:b2053;ecoc:C3026_11555;`
- `GeneID:93775138;946562;`
- `GO:GO:0008446; GO:0009242; GO:0042351; GO:0042803; GO:0070401`
- `EC:4.2.1.47`

## Notes

GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose dehydratase)
