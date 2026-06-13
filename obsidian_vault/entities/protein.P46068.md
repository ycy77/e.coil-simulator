---
entity_id: "protein.P46068"
entity_type: "protein"
name: "dsdC"
source_database: "UniProt"
source_id: "P46068"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dsdC b2364 JW2361"
---

# dsdC

`protein.P46068`

## Static

- Type: `protein`
- Source: `UniProt:P46068`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulates the expression of the dsdX-dsdA operon. {ECO:0000269|PubMed:7592420}.

## Biological Role

Component of DNA-binding transcriptional dual regulator DsdC (complex.ecocyc.CPLX0-7713).

## Annotation

FUNCTION: Regulates the expression of the dsdX-dsdA operon. {ECO:0000269|PubMed:7592420}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7713|complex.ecocyc.CPLX0-7713]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2364|gene.b2364]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46068`
- `KEGG:ecj:JW2361;eco:b2364;ecoc:C3026_13150;`
- `GeneID:948828;`
- `GO:GO:0003700; GO:0006351; GO:0043565`

## Notes

HTH-type transcriptional regulator DsdC (D-serine deaminase activator)
