---
entity_id: "protein.P0A962"
entity_type: "protein"
name: "ansA"
source_database: "UniProt"
source_id: "P0A962"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ansA b1767 JW1756"
---

# ansA

`protein.P0A962`

## Static

- Type: `protein`
- Source: `UniProt:P0A962`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

L-asparaginase 1 (EC 3.5.1.1) (L-asparaginase I) (L-ASNase I) (L-asparagine amidohydrolase I)

## Biological Role

Catalyzes L-asparagine amidohydrolase (reaction.R00485). Component of L-asparaginase 1 (complex.ecocyc.ANSA-CPLX).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

L-asparaginase 1 (EC 3.5.1.1) (L-asparaginase I) (L-ASNase I) (L-asparagine amidohydrolase I)

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00485|reaction.R00485]] `KEGG` `database` - via EC:3.5.1.1
- `is_component_of` --> [[complex.ecocyc.ANSA-CPLX|complex.ecocyc.ANSA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1767|gene.b1767]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A962`
- `KEGG:ecj:JW1756;eco:b1767;ecoc:C3026_10090;`
- `GeneID:93775984;946278;`
- `GO:GO:0004067; GO:0005737; GO:0005829; GO:0033345; GO:0042802; GO:0051289`
- `EC:3.5.1.1`

## Notes

L-asparaginase 1 (EC 3.5.1.1) (L-asparaginase I) (L-ASNase I) (L-asparagine amidohydrolase I)
