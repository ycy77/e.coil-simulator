---
entity_id: "protein.P31120"
entity_type: "protein"
name: "glmM"
source_database: "UniProt"
source_id: "P31120"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glmM mrsA yhbF b3176 JW3143"
---

# glmM

`protein.P31120`

## Static

- Type: `protein`
- Source: `UniProt:P31120`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of glucosamine-6-phosphate to glucosamine-1-phosphate. Can also catalyze the formation of glucose-6-P from glucose-1-P, although at a 1400-fold lower rate. {ECO:0000269|PubMed:10231382}.

## Biological Role

Component of phosphoglucosamine mutase (complex.ecocyc.CPLX0-8583).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of glucosamine-6-phosphate to glucosamine-1-phosphate. Can also catalyze the formation of glucose-6-P from glucose-1-P, although at a 1400-fold lower rate. {ECO:0000269|PubMed:10231382}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8583|complex.ecocyc.CPLX0-8583]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3176|gene.b3176]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31120`
- `KEGG:ecj:JW3143;eco:b3176;ecoc:C3026_17295;`
- `GeneID:75206032;947692;`
- `GO:GO:0000287; GO:0004615; GO:0005829; GO:0005975; GO:0006048; GO:0008966; GO:0009252; GO:0042802`
- `EC:5.4.2.10`

## Notes

Phosphoglucosamine mutase (EC 5.4.2.10)
