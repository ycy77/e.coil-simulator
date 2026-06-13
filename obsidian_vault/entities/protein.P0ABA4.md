---
entity_id: "protein.P0ABA4"
entity_type: "protein"
name: "atpH"
source_database: "UniProt"
source_id: "P0ABA4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01416, ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01416, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atpH papE uncH b3735 JW3713"
---

# atpH

`protein.P0ABA4`

## Static

- Type: `protein`
- Source: `UniProt:P0ABA4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01416, ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01416, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient. F-type ATPases consist of two structural domains, F(1) containing the extramembraneous catalytic core and F(0) containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain of F(1) is coupled via a rotary mechanism of the central stalk subunits to proton translocation.; FUNCTION: This protein is part of the stalk that links CF(0) to CF(1). It either transmits conformational changes from CF(0) to CF(1) or is implicated in proton conduction. The delta subunit is required for binding the F1 complex to the F0 complex. It may also block proton conduction through the Fo complex.

## Biological Role

Component of ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX), ATP synthase F1 complex (complex.ecocyc.F-1-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient. F-type ATPases consist of two structural domains, F(1) containing the extramembraneous catalytic core and F(0) containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain of F(1) is coupled via a rotary mechanism of the central stalk subunits to proton translocation.; FUNCTION: This protein is part of the stalk that links CF(0) to CF(1). It either transmits conformational changes from CF(0) to CF(1) or is implicated in proton conduction.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.F-1-CPLX|complex.ecocyc.F-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3735|gene.b3735]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABA4`
- `KEGG:ecj:JW3713;eco:b3735;ecoc:C3026_20240;`
- `GeneID:86861843;93778232;948254;`
- `GO:GO:0005886; GO:0015986; GO:0042777; GO:0045259; GO:0046933; GO:0046961`

## Notes

ATP synthase subunit delta (ATP synthase F(1) sector subunit delta) (F-type ATPase subunit delta) (F-ATPase subunit delta)
