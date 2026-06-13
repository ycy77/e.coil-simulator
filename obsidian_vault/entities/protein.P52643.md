---
entity_id: "protein.P52643"
entity_type: "protein"
name: "ldhA"
source_database: "UniProt"
source_id: "P52643"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ldhA hslI htpH b1380 JW1375"
---

# ldhA

`protein.P52643`

## Static

- Type: `protein`
- Source: `UniProt:P52643`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Fermentative lactate dehydrogenase. {ECO:0000269|PubMed:4297265}.

## Biological Role

Catalyzes (R)-lactate:NAD+ oxidoreductase (reaction.R00704). Component of D-lactate dehydrogenase (complex.ecocyc.CPLX0-8158).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Fermentative lactate dehydrogenase. {ECO:0000269|PubMed:4297265}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00704|reaction.R00704]] `KEGG` `database` - via EC:1.1.1.28
- `is_component_of` --> [[complex.ecocyc.CPLX0-8158|complex.ecocyc.CPLX0-8158]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1380|gene.b1380]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52643`
- `KEGG:ecj:JW1375;eco:b1380;ecoc:C3026_08065;`
- `GeneID:946315;`
- `GO:GO:0005829; GO:0006089; GO:0008720; GO:0009408; GO:0019664; GO:0042802; GO:0051289; GO:0070404`
- `EC:1.1.1.28`

## Notes

D-lactate dehydrogenase (D-LDH) (EC 1.1.1.28) (Fermentative lactate dehydrogenase)
