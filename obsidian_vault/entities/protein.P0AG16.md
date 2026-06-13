---
entity_id: "protein.P0AG16"
entity_type: "protein"
name: "purF"
source_database: "UniProt"
source_id: "P0AG16"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purF b2312 JW2309"
---

# purF

`protein.P0AG16`

## Static

- Type: `protein`
- Source: `UniProt:P0AG16`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of phosphoribosylamine from phosphoribosylpyrophosphate (PRPP) and glutamine. Can also use NH(3) in place of glutamine. {ECO:0000269|PubMed:372191}.

## Biological Role

Component of amidophosphoribosyltransferase (complex.ecocyc.PRPPAMIDOTRANS-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of phosphoribosylamine from phosphoribosylpyrophosphate (PRPP) and glutamine. Can also use NH(3) in place of glutamine. {ECO:0000269|PubMed:372191}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PRPPAMIDOTRANS-CPLX|complex.ecocyc.PRPPAMIDOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2312|gene.b2312]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG16`
- `KEGG:ecj:JW2309;eco:b2312;ecoc:C3026_12890;`
- `GeneID:93774862;946794;`
- `GO:GO:0000287; GO:0004044; GO:0005737; GO:0005829; GO:0006164; GO:0006189; GO:0006541; GO:0009113; GO:0016757; GO:0042802; GO:0097216`
- `EC:2.4.2.14`

## Notes

Amidophosphoribosyltransferase (ATase) (EC 2.4.2.14) (Glutamine phosphoribosylpyrophosphate amidotransferase) (GPATase)
