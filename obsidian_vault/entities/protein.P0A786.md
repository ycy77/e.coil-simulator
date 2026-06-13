---
entity_id: "protein.P0A786"
entity_type: "protein"
name: "pyrB"
source_database: "UniProt"
source_id: "P0A786"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pyrB b4245 JW4204"
---

# pyrB

`protein.P0A786`

## Static

- Type: `protein`
- Source: `UniProt:P0A786`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the condensation of carbamoyl phosphate and aspartate to form carbamoyl aspartate and inorganic phosphate, the committed step in the de novo pyrimidine nucleotide biosynthesis pathway. {ECO:0000255|HAMAP-Rule:MF_00001, ECO:0000269|PubMed:13319326}.

## Biological Role

Component of aspartate carbamoyltransferase catalytic subunit (complex.ecocyc.ASPCARBCAT-TRIMER), aspartate carbamoyltransferase (complex.ecocyc.ASPCARBTRANS-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the condensation of carbamoyl phosphate and aspartate to form carbamoyl aspartate and inorganic phosphate, the committed step in the de novo pyrimidine nucleotide biosynthesis pathway. {ECO:0000255|HAMAP-Rule:MF_00001, ECO:0000269|PubMed:13319326}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ASPCARBCAT-TRIMER|complex.ecocyc.ASPCARBCAT-TRIMER]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.ASPCARBTRANS-CPLX|complex.ecocyc.ASPCARBTRANS-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b4245|gene.b4245]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A786`
- `KEGG:ecj:JW4204;eco:b4245;ecoc:C3026_22910;`
- `GeneID:93777579;948767;`
- `GO:GO:0004070; GO:0005737; GO:0005829; GO:0006207; GO:0006541; GO:0009347; GO:0016597; GO:0042802; GO:0044205; GO:0070207`
- `EC:2.1.3.2`

## Notes

Aspartate carbamoyltransferase catalytic subunit (EC 2.1.3.2) (Aspartate transcarbamylase) (ATCase)
