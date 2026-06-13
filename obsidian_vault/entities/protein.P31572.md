---
entity_id: "protein.P31572"
entity_type: "protein"
name: "caiB"
source_database: "UniProt"
source_id: "P31572"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01050}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "caiB yaaN b0038 JW0037"
---

# caiB

`protein.P31572`

## Static

- Type: `protein`
- Source: `UniProt:P31572`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01050}.

## Enriched Summary

FUNCTION: Catalyzes the reversible transfer of the CoA moiety from gamma-butyrobetainyl-CoA to L-carnitine to generate L-carnitinyl-CoA and gamma-butyrobetaine. Is also able to catalyze the reversible transfer of the CoA moiety from gamma-butyrobetainyl-CoA or L-carnitinyl-CoA to crotonobetaine to generate crotonobetainyl-CoA. {ECO:0000255|HAMAP-Rule:MF_01050, ECO:0000269|PubMed:11551212}.

## Biological Role

Component of γ-butyrobetainyl-CoA:carnitine CoA transferase (complex.ecocyc.CARNDEHYDRA-CPLX).

## Annotation

FUNCTION: Catalyzes the reversible transfer of the CoA moiety from gamma-butyrobetainyl-CoA to L-carnitine to generate L-carnitinyl-CoA and gamma-butyrobetaine. Is also able to catalyze the reversible transfer of the CoA moiety from gamma-butyrobetainyl-CoA or L-carnitinyl-CoA to crotonobetaine to generate crotonobetainyl-CoA. {ECO:0000255|HAMAP-Rule:MF_01050, ECO:0000269|PubMed:11551212}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CARNDEHYDRA-CPLX|complex.ecocyc.CARNDEHYDRA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0038|gene.b0038]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31572`
- `KEGG:ecj:JW0037;eco:b0038;ecoc:C3026_00200;`
- `GeneID:948997;`
- `GO:GO:0005737; GO:0008735; GO:0042413`
- `EC:2.8.3.21`

## Notes

L-carnitine CoA-transferase (EC 2.8.3.21) (Crotonobetainyl-CoA:carnitine CoA-transferase)
