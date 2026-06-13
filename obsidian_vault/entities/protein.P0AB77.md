---
entity_id: "protein.P0AB77"
entity_type: "protein"
name: "kbl"
source_database: "UniProt"
source_id: "P0AB77"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kbl b3617 JW3592"
---

# kbl

`protein.P0AB77`

## Static

- Type: `protein`
- Source: `UniProt:P0AB77`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the cleavage of 2-amino-3-ketobutyrate to glycine and acetyl-CoA. {ECO:0000255|HAMAP-Rule:MF_00985, ECO:0000269|PubMed:2104756}.

## Biological Role

Catalyzes acetyl-CoA:glycine C-acetyltransferase (reaction.R00371). Component of 2-amino-3-ketobutyrate CoA ligase (complex.ecocyc.AKBLIG-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the cleavage of 2-amino-3-ketobutyrate to glycine and acetyl-CoA. {ECO:0000255|HAMAP-Rule:MF_00985, ECO:0000269|PubMed:2104756}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00371|reaction.R00371]] `KEGG` `database` - via EC:2.3.1.29
- `is_component_of` --> [[complex.ecocyc.AKBLIG-CPLX|complex.ecocyc.AKBLIG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3617|gene.b3617]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB77`
- `KEGG:ecj:JW3592;eco:b3617;ecoc:C3026_19610;`
- `GeneID:75173814;75202189;948138;`
- `GO:GO:0005737; GO:0005829; GO:0008890; GO:0016874; GO:0019518; GO:0030170; GO:0046872`
- `EC:2.3.1.29`

## Notes

2-amino-3-ketobutyrate coenzyme A ligase (AKB ligase) (EC 2.3.1.29) (Glycine acetyltransferase)
