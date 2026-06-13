---
entity_id: "protein.P0AGM7"
entity_type: "protein"
name: "uraA"
source_database: "UniProt"
source_id: "P0AGM7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:21423164}; Multi-pass membrane protein {ECO:0000269|PubMed:21423164}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uraA b2497 JW2482"
---

# uraA

`protein.P0AGM7`

## Static

- Type: `protein`
- Source: `UniProt:P0AGM7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:21423164}; Multi-pass membrane protein {ECO:0000269|PubMed:21423164}.

## Enriched Summary

FUNCTION: Transport of uracil in the cell. {ECO:0000269|PubMed:21423164, ECO:0000269|PubMed:7721693}.

## Biological Role

Component of uracil transporter UraA (complex.ecocyc.CPLX0-8247).

## Annotation

FUNCTION: Transport of uracil in the cell. {ECO:0000269|PubMed:21423164, ECO:0000269|PubMed:7721693}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8247|complex.ecocyc.CPLX0-8247]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2497|gene.b2497]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGM7`
- `KEGG:ecj:JW2482;eco:b2497;ecoc:C3026_13850;`
- `GeneID:86860618;93774639;946978;`
- `GO:GO:0005886; GO:0015210; GO:0015505; GO:0015857; GO:0016020; GO:0042803; GO:0098721`

## Notes

Uracil permease (Uracil transporter) (Uracil/H(+) symporter UraA)
