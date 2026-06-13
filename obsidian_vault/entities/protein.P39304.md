---
entity_id: "protein.P39304"
entity_type: "protein"
name: "ulaD"
source_database: "UniProt"
source_id: "P39304"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ulaD sgaH yjfV b4196 JW4154"
---

# ulaD

`protein.P39304`

## Static

- Type: `protein`
- Source: `UniProt:P39304`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the decarboxylation of 3-keto-L-gulonate-6-P into L-xylulose-5-P. Is involved in the anaerobic L-ascorbate utilization. {ECO:0000269|PubMed:11741871}.

## Biological Role

Component of 3-keto-L-gulonate-6-phosphate decarboxylase UlaD (complex.ecocyc.CPLX0-7744).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylation of 3-keto-L-gulonate-6-P into L-xylulose-5-P. Is involved in the anaerobic L-ascorbate utilization. {ECO:0000269|PubMed:11741871}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7744|complex.ecocyc.CPLX0-7744]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4196|gene.b4196]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39304`
- `KEGG:ecj:JW4154;eco:b4196;ecoc:C3026_22665;`
- `GeneID:948714;`
- `GO:GO:0000287; GO:0004590; GO:0006207; GO:0019854; GO:0033982`
- `EC:4.1.1.85`

## Notes

3-keto-L-gulonate-6-phosphate decarboxylase UlaD (EC 4.1.1.85) (3-dehydro-L-gulonate-6-phosphate decarboxylase) (KGPDC) (L-ascorbate utilization protein D)
