---
entity_id: "protein.P16456"
entity_type: "protein"
name: "selD"
source_database: "UniProt"
source_id: "P16456"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "selD fdhB b1764 JW1753"
---

# selD

`protein.P16456`

## Static

- Type: `protein`
- Source: `UniProt:P16456`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Synthesizes selenophosphate from selenide and ATP. {ECO:0000255|HAMAP-Rule:MF_00625, ECO:0000269|PubMed:22081394, ECO:0000269|PubMed:2405383}.

## Biological Role

Component of selenide, water dikinase (complex.ecocyc.CPLX0-7957).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Synthesizes selenophosphate from selenide and ATP. {ECO:0000255|HAMAP-Rule:MF_00625, ECO:0000269|PubMed:22081394, ECO:0000269|PubMed:2405383}.

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7957|complex.ecocyc.CPLX0-7957]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1764|gene.b1764]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16456`
- `KEGG:ecj:JW1753;eco:b1764;ecoc:C3026_10065;`
- `GeneID:75057654;946768;`
- `GO:GO:0000287; GO:0004756; GO:0005524; GO:0005737; GO:0005829; GO:0016260; GO:0042802; GO:0042803; GO:0070329`
- `EC:2.7.9.3`

## Notes

Selenide, water dikinase (EC 2.7.9.3) (Selenium donor protein) (Selenophosphate synthase)
