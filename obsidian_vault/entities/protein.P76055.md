---
entity_id: "protein.P76055"
entity_type: "protein"
name: "ttcA"
source_database: "UniProt"
source_id: "P76055"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01850, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ttcA ydaO b1344 JW1338"
---

# ttcA

`protein.P76055`

## Static

- Type: `protein`
- Source: `UniProt:P76055`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01850, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent 2-thiolation of cytidine in position 32 of tRNA, to form 2-thiocytidine (s(2)C32). The sulfur atoms are provided by the cysteine/cysteine desulfurase (IscS) system. {ECO:0000255|HAMAP-Rule:MF_01850, ECO:0000269|PubMed:24914049, ECO:0000305|PubMed:14729701}.

## Biological Role

Component of tRNA cytosine32 2-sulfurtransferase TtcA (complex.ecocyc.CPLX0-8124).

## Annotation

FUNCTION: Catalyzes the ATP-dependent 2-thiolation of cytidine in position 32 of tRNA, to form 2-thiocytidine (s(2)C32). The sulfur atoms are provided by the cysteine/cysteine desulfurase (IscS) system. {ECO:0000255|HAMAP-Rule:MF_01850, ECO:0000269|PubMed:24914049, ECO:0000305|PubMed:14729701}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8124|complex.ecocyc.CPLX0-8124]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1344|gene.b1344]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76055`
- `KEGG:ecj:JW1338;eco:b1344;ecoc:C3026_07875;`
- `GeneID:948967;`
- `GO:GO:0000049; GO:0000287; GO:0005524; GO:0005829; GO:0006400; GO:0016783; GO:0034227; GO:0042803; GO:0051539`
- `EC:2.8.1.-`

## Notes

tRNA-cytidine(32) 2-sulfurtransferase (EC 2.8.1.-) (Two-thiocytidine biosynthesis protein A) (tRNA 2-thiocytidine biosynthesis protein TtcA)
