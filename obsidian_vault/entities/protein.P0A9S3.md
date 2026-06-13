---
entity_id: "protein.P0A9S3"
entity_type: "protein"
name: "gatD"
source_database: "UniProt"
source_id: "P0A9S3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gatD b2091 JW2075"
---

# gatD

`protein.P0A9S3`

## Static

- Type: `protein`
- Source: `UniProt:P0A9S3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts galactitol 1-phosphate to D-tagatose 6-phosphate. {ECO:0000269|PubMed:13331868}.

## Biological Role

Component of galactitol-1-phosphate 5-dehydrogenase (complex.ecocyc.CPLX0-8186).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Converts galactitol 1-phosphate to D-tagatose 6-phosphate. {ECO:0000269|PubMed:13331868}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8186|complex.ecocyc.CPLX0-8186]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2091|gene.b2091]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9S3`
- `KEGG:ecj:JW2075;eco:b2091;ecoc:C3026_11740;`
- `GeneID:946598;`
- `GO:GO:0005829; GO:0008270; GO:0008868; GO:0019404; GO:0042802; GO:0042803`
- `EC:1.1.1.251`

## Notes

Galactitol 1-phosphate 5-dehydrogenase (EC 1.1.1.251)
