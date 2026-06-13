---
entity_id: "protein.P00805"
entity_type: "protein"
name: "ansB"
source_database: "UniProt"
source_id: "P00805"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ansB b2957 JW2924"
---

# ansB

`protein.P00805`

## Static

- Type: `protein`
- Source: `UniProt:P00805`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

L-asparaginase 2 (EC 3.5.1.1) (L-asparaginase II) (L-ASNase II) (L-asparagine amidohydrolase II) (Colaspase)

## Biological Role

Catalyzes L-asparagine amidohydrolase (reaction.R00485). Component of L-asparaginase 2 (complex.ecocyc.ANSB-CPLX).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

L-asparaginase 2 (EC 3.5.1.1) (L-asparaginase II) (L-ASNase II) (L-asparagine amidohydrolase II) (Colaspase)

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00485|reaction.R00485]] `KEGG` `database` - via EC:3.5.1.1
- `is_component_of` --> [[complex.ecocyc.ANSB-CPLX|complex.ecocyc.ANSB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2957|gene.b2957]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00805`
- `KEGG:ecj:JW2924;eco:b2957;ecoc:C3026_16180;`
- `GeneID:947454;`
- `GO:GO:0004067; GO:0006530; GO:0030288; GO:0032991; GO:0042597; GO:0042802; GO:0051289`
- `EC:3.5.1.1`

## Notes

L-asparaginase 2 (EC 3.5.1.1) (L-asparaginase II) (L-ASNase II) (L-asparagine amidohydrolase II) (Colaspase)
