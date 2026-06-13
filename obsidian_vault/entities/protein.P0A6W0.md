---
entity_id: "protein.P0A6W0"
entity_type: "protein"
name: "glsA2"
source_database: "UniProt"
source_id: "P0A6W0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glsA2 yneH b1524 JW1517"
---

# glsA2

`protein.P0A6W0`

## Static

- Type: `protein`
- Source: `UniProt:P0A6W0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Glutaminase 2 (EC 3.5.1.2) GlsB (YneH) is a glutaminase that is highly selective for L-glutamine. Based on the pH profile of the enzymatic activity, GlsB was proposed to correspond to the previously identified GLUTAMINB-CPLX of E. coli B. Glutamine binding exhibits positive cooperativity . A glsB deletion mutant grows two times slower than wild-type on glutamine as the sole source of carbon and nitrogen . A ΔglsB mutant has no defect in glutamine-dependent acid resistance . Review:

## Biological Role

Catalyzes L-glutamine amidohydrolase (reaction.R00256). Component of glutaminase 2 (complex.ecocyc.CPLX0-7695).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

Glutaminase 2 (EC 3.5.1.2)

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - via EC:3.5.1.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7695|complex.ecocyc.CPLX0-7695]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1524|gene.b1524]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6W0`
- `KEGG:ecj:JW1517;eco:b1524;ecoc:C3026_08810;`
- `GeneID:93775688;944973;`
- `GO:GO:0004359; GO:0006537; GO:0006543; GO:0042803; GO:0045926`
- `EC:3.5.1.2`

## Notes

Glutaminase 2 (EC 3.5.1.2)
