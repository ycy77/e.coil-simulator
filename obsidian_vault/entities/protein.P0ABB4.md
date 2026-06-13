---
entity_id: "protein.P0ABB4"
entity_type: "protein"
name: "atpD"
source_database: "UniProt"
source_id: "P0ABB4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atpD papB uncD b3732 JW3710"
---

# atpD

`protein.P0ABB4`

## Static

- Type: `protein`
- Source: `UniProt:P0ABB4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The catalytic sites are hosted primarily by the beta subunits.

## Biological Role

Catalyzes ATP phosphohydrolase (reaction.R00086). Component of ATP synthase F1 complex subunit β (complex.ecocyc.ATPD-CPLX), ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX), ATP synthase F1 complex (complex.ecocyc.F-1-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The catalytic sites are hosted primarily by the beta subunits.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00086|reaction.R00086]] `KEGG` `database` - via EC:7.1.2.2
- `is_component_of` --> [[complex.ecocyc.ATPD-CPLX|complex.ecocyc.ATPD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` --> [[complex.ecocyc.F-1-CPLX|complex.ecocyc.F-1-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3732|gene.b3732]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABB4`
- `KEGG:ecj:JW3710;eco:b3732;ecoc:C3026_20225;`
- `GeneID:86861840;93778235;948244;`
- `GO:GO:0005524; GO:0005886; GO:0016020; GO:0042777; GO:0045259; GO:0046933; GO:0046961`
- `EC:7.1.2.2`

## Notes

ATP synthase subunit beta (EC 7.1.2.2) (ATP synthase F1 sector subunit beta) (F-ATPase subunit beta)
