---
entity_id: "protein.P32170"
entity_type: "protein"
name: "rhaA"
source_database: "UniProt"
source_id: "P32170"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00541, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhaA b3903 JW5561"
---

# rhaA

`protein.P32170`

## Static

- Type: `protein`
- Source: `UniProt:P32170`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00541, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the interconversion of L-rhamnose and L-rhamnulose (PubMed:14243758, PubMed:1650346, PubMed:2558952, PubMed:8564401). Can also catalyze the isomerization of L-lyxose to L-xylulose (PubMed:1650346). {ECO:0000269|PubMed:14243758, ECO:0000269|PubMed:1650346, ECO:0000269|PubMed:2558952, ECO:0000269|PubMed:8564401}. L-rhamnose isomerase (RhaA) catalyzes the first step in the utilization of the deoxyhexose sugar rhamnose. L-rhamnose isomerase is also capable of using L-lyxose as a substrate . Conditioned on activation of LYXK-CPLX, RhaA contributes to E. coli's ability to metabolize the uncommon sugar, L-lyxose . Crystal structures of L-rhamnose isomerase have been determined. Despite low sequence similarity, the enzyme shows structural similarity to xylose isomerase from Streptomyces rubiginosus. The data suggests the possibility of a metal-mediated hydride shift reaction mechanism . Expression of rhaA is induced by L-rhamnose . L-lyxose can also induce expression of rhaA . rhaA mutants can not utilize rhamnose as a source of carbon .

## Biological Role

Component of L-rhamnose isomerase (complex.ecocyc.CPLX0-7652).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion of L-rhamnose and L-rhamnulose (PubMed:14243758, PubMed:1650346, PubMed:2558952, PubMed:8564401). Can also catalyze the isomerization of L-lyxose to L-xylulose (PubMed:1650346). {ECO:0000269|PubMed:14243758, ECO:0000269|PubMed:1650346, ECO:0000269|PubMed:2558952, ECO:0000269|PubMed:8564401}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7652|complex.ecocyc.CPLX0-7652]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3903|gene.b3903]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32170`
- `KEGG:ecj:JW5561;eco:b3903;ecoc:C3026_21100;`
- `GeneID:948400;`
- `GO:GO:0005737; GO:0008270; GO:0008740; GO:0019301; GO:0019324; GO:0030145; GO:0032991; GO:0033296; GO:0042802; GO:0051289`
- `EC:5.3.1.14`

## Notes

L-rhamnose isomerase (RhamIso) (EC 5.3.1.14)
