---
entity_id: "protein.P06988"
entity_type: "protein"
name: "hisD"
source_database: "UniProt"
source_id: "P06988"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisD b2020 JW2002"
---

# hisD

`protein.P06988`

## Static

- Type: `protein`
- Source: `UniProt:P06988`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the sequential NAD-dependent oxidations of L-histidinol to L-histidinaldehyde and then to L-histidine. {ECO:0000255|HAMAP-Rule:MF_01024}.

## Biological Role

Catalyzes L-histidinol:NAD+ oxidoreductase (reaction.R01158), L-histidinal:NAD+ oxidoreductase (reaction.R01163). Component of histidinol dehydrogenase (complex.ecocyc.HISTDEHYD-CPLX).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the sequential NAD-dependent oxidations of L-histidinol to L-histidinaldehyde and then to L-histidine. {ECO:0000255|HAMAP-Rule:MF_01024}.

## Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R01158|reaction.R01158]] `KEGG` `database` - via EC:1.1.1.23
- `catalyzes` --> [[reaction.R01163|reaction.R01163]] `KEGG` `database` - via EC:1.1.1.23
- `is_component_of` --> [[complex.ecocyc.HISTDEHYD-CPLX|complex.ecocyc.HISTDEHYD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2020|gene.b2020]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06988`
- `KEGG:ecj:JW2002;eco:b2020;ecoc:C3026_11390;`
- `GeneID:946531;`
- `GO:GO:0000105; GO:0004399; GO:0005737; GO:0005829; GO:0008270; GO:0030145; GO:0046872; GO:0051287`
- `EC:1.1.1.23`

## Notes

Histidinol dehydrogenase (HDH) (EC 1.1.1.23)
