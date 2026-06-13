---
entity_id: "protein.P26646"
entity_type: "protein"
name: "acuI"
source_database: "UniProt"
source_id: "P26646"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acuI yhdH b3253 JW3222"
---

# acuI

`protein.P26646`

## Static

- Type: `protein`
- Source: `UniProt:P26646`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Probably catalyzes the NADPH-dependent reduction of acrylyl-CoA to propanoyl-CoA. {ECO:0000269|PubMed:22563425}.

## Biological Role

Component of acrylyl-CoA reductase (complex.ecocyc.CPLX0-8121).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Probably catalyzes the NADPH-dependent reduction of acrylyl-CoA to propanoyl-CoA. {ECO:0000269|PubMed:22563425}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8121|complex.ecocyc.CPLX0-8121]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3253|gene.b3253]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P26646`
- `KEGG:ecj:JW3222;eco:b3253;ecoc:C3026_17690;`
- `GeneID:947848;`
- `GO:GO:0005737; GO:0042803; GO:0043957`
- `EC:1.3.1.84`

## Notes

Probable acrylyl-CoA reductase AcuI (EC 1.3.1.84) (Acryloyl-coenzyme A reductase AcuI)
