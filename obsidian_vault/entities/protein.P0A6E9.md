---
entity_id: "protein.P0A6E9"
entity_type: "protein"
name: "bioD2"
source_database: "UniProt"
source_id: "P0A6E9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00336}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bioD2 ynfK b1593 JW5264"
---

# bioD2

`protein.P0A6E9`

## Static

- Type: `protein`
- Source: `UniProt:P0A6E9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00336}.

## Enriched Summary

FUNCTION: Catalyzes a mechanistically unusual reaction, the ATP-dependent insertion of CO2 between the N7 and N8 nitrogen atoms of 7,8-diaminopelargonic acid (DAPA, also called 7,8-diammoniononanoate) to form a ureido ring. {ECO:0000255|HAMAP-Rule:MF_00336}.

## Biological Role

Catalyzes 7,8-diaminononanoate:carbon-dioxide cyclo-ligase (reaction.R03182). Component of dethiobiotin synthetase BidA (complex.ecocyc.CPLX0-8613).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes a mechanistically unusual reaction, the ATP-dependent insertion of CO2 between the N7 and N8 nitrogen atoms of 7,8-diaminopelargonic acid (DAPA, also called 7,8-diammoniononanoate) to form a ureido ring. {ECO:0000255|HAMAP-Rule:MF_00336}.

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03182|reaction.R03182]] `KEGG` `database` - via EC:6.3.3.3
- `is_component_of` --> [[complex.ecocyc.CPLX0-8613|complex.ecocyc.CPLX0-8613]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1593|gene.b1593]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6E9`
- `KEGG:ecj:JW5264;eco:b1593;ecoc:C3026_09175;`
- `GeneID:75204436;944927;`
- `GO:GO:0000287; GO:0004141; GO:0005524; GO:0005829; GO:0009102; GO:0042803`
- `EC:6.3.3.3`

## Notes

ATP-dependent dethiobiotin synthetase BioD 2 (EC 6.3.3.3) (DTB synthetase 2) (DTBS 2) (Dethiobiotin synthase 2)
