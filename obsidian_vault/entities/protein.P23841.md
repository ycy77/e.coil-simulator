---
entity_id: "protein.P23841"
entity_type: "protein"
name: "xapR"
source_database: "UniProt"
source_id: "P23841"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xapR pndR yfeB b2405 JW2396"
---

# xapR

`protein.P23841`

## Static

- Type: `protein`
- Source: `UniProt:P23841`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Positive regulator required for the expression of xapA and xapB. Binds to the inducer xanthosine.

## Biological Role

Component of XapR-xanthosine DNA-binding transcriptional activator (complex.ecocyc.CPLX0-7681).

## Annotation

FUNCTION: Positive regulator required for the expression of xapA and xapB. Binds to the inducer xanthosine.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7681|complex.ecocyc.CPLX0-7681]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b2405|gene.b2405]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23841`
- `KEGG:ecj:JW2396;eco:b2405;ecoc:C3026_13365;`
- `GeneID:946862;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0032993; GO:0045893`

## Notes

HTH-type transcriptional regulator XapR (Xanthosine operon regulatory protein)
