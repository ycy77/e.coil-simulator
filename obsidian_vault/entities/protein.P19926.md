---
entity_id: "protein.P19926"
entity_type: "protein"
name: "agp"
source_database: "UniProt"
source_id: "P19926"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "agp b1002 JW0987"
---

# agp

`protein.P19926`

## Static

- Type: `protein`
- Source: `UniProt:P19926`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Absolutely required for the growth of E.coli in a high-phosphate medium containing G-1-P as the sole carbon source.

## Biological Role

Catalyzes D-glucose-1-phosphate phosphohydrolase (reaction.R00304). Component of glucose-1-phosphatase (complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Absolutely required for the growth of E.coli in a high-phosphate medium containing G-1-P as the sole carbon source.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00304|reaction.R00304]] `KEGG` `database` - via EC:3.1.3.10
- `is_component_of` --> [[complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX|complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1002|gene.b1002]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19926`
- `KEGG:ecj:JW0987;eco:b1002;ecoc:C3026_06100;`
- `GeneID:945773;`
- `GO:GO:0006007; GO:0008877; GO:0016158; GO:0030288; GO:0050308`
- `EC:3.1.3.10`

## Notes

Glucose-1-phosphatase (G1Pase) (EC 3.1.3.10)
