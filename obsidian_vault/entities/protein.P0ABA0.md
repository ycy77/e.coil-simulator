---
entity_id: "protein.P0ABA0"
entity_type: "protein"
name: "atpF"
source_database: "UniProt"
source_id: "P0ABA0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01398}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01398}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atpF papF uncF b3736 JW3714"
---

# atpF

`protein.P0ABA0`

## Static

- Type: `protein`
- Source: `UniProt:P0ABA0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01398}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01398}.

## Enriched Summary

FUNCTION: F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient. F-type ATPases consist of two structural domains, F(1) containing the extramembraneous catalytic core and F(0) containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain of F(1) is coupled via a rotary mechanism of the central stalk subunits to proton translocation. {ECO:0000255|HAMAP-Rule:MF_01398}.; FUNCTION: Component of the F(0) channel, it forms part of the peripheral stalk, linking F(1) to F(0). {ECO:0000255|HAMAP-Rule:MF_01398}.

## Biological Role

Component of ATP synthase Fo complex - subunit b (complex.ecocyc.ATPF-CPLX), ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX), ATP synthase Fo complex (complex.ecocyc.F-O-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient. F-type ATPases consist of two structural domains, F(1) containing the extramembraneous catalytic core and F(0) containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain of F(1) is coupled via a rotary mechanism of the central stalk subunits to proton translocation. {ECO:0000255|HAMAP-Rule:MF_01398}.; FUNCTION: Component of the F(0) channel, it forms part of the peripheral stalk, linking F(1) to F(0). {ECO:0000255|HAMAP-Rule:MF_01398}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.ATPF-CPLX|complex.ecocyc.ATPF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.F-O-CPLX|complex.ecocyc.F-O-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3736|gene.b3736]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABA0`
- `KEGG:ecj:JW3714;eco:b3736;ecoc:C3026_20245;`
- `GeneID:86861844;93778231;948247;`
- `GO:GO:0005886; GO:0042777; GO:0045259; GO:0046933; GO:0046961`

## Notes

ATP synthase subunit b (ATP synthase F(0) sector subunit b) (ATPase subunit I) (F-type ATPase subunit b) (F-ATPase subunit b)
