---
entity_id: "protein.P0ABB0"
entity_type: "protein"
name: "atpA"
source_database: "UniProt"
source_id: "P0ABB0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01346, ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01346, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atpA papA uncA b3734 JW3712"
---

# atpA

`protein.P0ABB0`

## Static

- Type: `protein`
- Source: `UniProt:P0ABB0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01346, ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01346, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The alpha chain is a regulatory subunit.

## Biological Role

Catalyzes ATP phosphohydrolase (reaction.R00086). Component of ATP synthase F1 complex subunit α (complex.ecocyc.ATPA-CPLX), ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX), ATP synthase F1 complex (complex.ecocyc.F-1-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The alpha chain is a regulatory subunit.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00086|reaction.R00086]] `KEGG` `database` - via EC:7.1.2.2
- `is_component_of` --> [[complex.ecocyc.ATPA-CPLX|complex.ecocyc.ATPA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` --> [[complex.ecocyc.F-1-CPLX|complex.ecocyc.F-1-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3734|gene.b3734]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABB0`
- `KEGG:ecj:JW3712;eco:b3734;ecoc:C3026_20235;`
- `GeneID:86861842;93778233;948242;`
- `GO:GO:0005524; GO:0005886; GO:0015986; GO:0016020; GO:0042777; GO:0043531; GO:0045259; GO:0046933`
- `EC:7.1.2.2`

## Notes

ATP synthase subunit alpha (EC 7.1.2.2) (ATP synthase F1 sector subunit alpha) (F-ATPase subunit alpha)
