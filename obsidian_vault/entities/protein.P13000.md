---
entity_id: "protein.P13000"
entity_type: "protein"
name: "bioD1"
source_database: "UniProt"
source_id: "P13000"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00336}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bioD1 b0778 JW0761"
---

# bioD1

`protein.P13000`

## Static

- Type: `protein`
- Source: `UniProt:P13000`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00336}.

## Enriched Summary

FUNCTION: Catalyzes a mechanistically unusual reaction, the ATP-dependent insertion of CO2 between the N7 and N8 nitrogen atoms of 7,8-diaminopelargonic acid (DAPA, also called 7,8-diammoniononanoate) to form a ureido ring. Only CTP can partially replace ATP while diaminobiotin is only 37% as effective as 7,8-diaminopelargonic acid (PubMed:4892372, PubMed:4921568). In another study both CTP and GTP (but not ITP, TTP or UTP) can partially replace ATP (PubMed:25801336). {ECO:0000269|PubMed:25801336, ECO:0000269|PubMed:4892372, ECO:0000269|PubMed:4921568}.

## Biological Role

Catalyzes 7,8-diaminononanoate:carbon-dioxide cyclo-ligase (reaction.R03182). Component of dethiobiotin synthetase (complex.ecocyc.DETHIOBIOTIN-SYN-CPLX).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes a mechanistically unusual reaction, the ATP-dependent insertion of CO2 between the N7 and N8 nitrogen atoms of 7,8-diaminopelargonic acid (DAPA, also called 7,8-diammoniononanoate) to form a ureido ring. Only CTP can partially replace ATP while diaminobiotin is only 37% as effective as 7,8-diaminopelargonic acid (PubMed:4892372, PubMed:4921568). In another study both CTP and GTP (but not ITP, TTP or UTP) can partially replace ATP (PubMed:25801336). {ECO:0000269|PubMed:25801336, ECO:0000269|PubMed:4892372, ECO:0000269|PubMed:4921568}.

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03182|reaction.R03182]] `KEGG` `database` - via EC:6.3.3.3
- `is_component_of` --> [[complex.ecocyc.DETHIOBIOTIN-SYN-CPLX|complex.ecocyc.DETHIOBIOTIN-SYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0778|gene.b0778]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13000`
- `KEGG:ecj:JW0761;eco:b0778;ecoc:C3026_04940;`
- `GO:GO:0000287; GO:0004141; GO:0005524; GO:0005829; GO:0009102; GO:0042803`
- `EC:6.3.3.3`

## Notes

ATP-dependent dethiobiotin synthetase BioD 1 (EC 6.3.3.3) (DTB synthetase 1) (DTBS 1) (Dethiobiotin synthase 1)
