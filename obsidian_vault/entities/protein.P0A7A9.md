---
entity_id: "protein.P0A7A9"
entity_type: "protein"
name: "ppa"
source_database: "UniProt"
source_id: "P0A7A9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00209}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppa b4226 JW4185"
---

# ppa

`protein.P0A7A9`

## Static

- Type: `protein`
- Source: `UniProt:P0A7A9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00209}.

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of inorganic pyrophosphate (PPi) forming two phosphate ions. {ECO:0000255|HAMAP-Rule:MF_00209}.

## Biological Role

Catalyzes diphosphate phosphohydrolase; (reaction.R00004). Component of inorganic pyrophosphatase (complex.ecocyc.CPLX0-243).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of inorganic pyrophosphate (PPi) forming two phosphate ions. {ECO:0000255|HAMAP-Rule:MF_00209}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00004|reaction.R00004]] `KEGG` `database` - via EC:3.6.1.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-243|complex.ecocyc.CPLX0-243]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b4226|gene.b4226]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7A9`
- `KEGG:ecj:JW4185;eco:b4226;ecoc:C3026_22820;`
- `GeneID:93777598;948748;`
- `GO:GO:0000287; GO:0004427; GO:0005829; GO:0006796; GO:0008270; GO:0016020; GO:0050355`
- `EC:3.6.1.1`

## Notes

Inorganic pyrophosphatase (EC 3.6.1.1) (Pyrophosphate phospho-hydrolase) (PPase)
