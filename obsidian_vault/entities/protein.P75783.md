---
entity_id: "protein.P75783"
entity_type: "protein"
name: "ybiO"
source_database: "UniProt"
source_id: "P75783"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22874652}; Multi-pass membrane protein {ECO:0000269|PubMed:22874652}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybiO b0808 JW5108"
---

# ybiO

`protein.P75783`

## Static

- Type: `protein`
- Source: `UniProt:P75783`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22874652}; Multi-pass membrane protein {ECO:0000269|PubMed:22874652}.

## Enriched Summary

FUNCTION: Mechanosensitive channel that protects cells against hypoosmotic stress when highly overexpressed. {ECO:0000269|PubMed:22874652}.

## Biological Role

Component of moderate conductance mechanosensitive channel YbiO (complex.ecocyc.CPLX0-7983).

## Annotation

FUNCTION: Mechanosensitive channel that protects cells against hypoosmotic stress when highly overexpressed. {ECO:0000269|PubMed:22874652}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7983|complex.ecocyc.CPLX0-7983]] `EcoCyc` `database` - EcoCyc component coefficient=7 | EcoCyc protcplxs.col coefficient=7

## Incoming Edges (1)

- `encodes` <-- [[gene.b0808|gene.b0808]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75783`
- `KEGG:ecj:JW5108;eco:b0808;ecoc:C3026_05090;`
- `GeneID:75170874;945935;`
- `GO:GO:0005886; GO:0008381; GO:0071470`

## Notes

Moderate conductance mechanosensitive channel YbiO
