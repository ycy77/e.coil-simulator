---
entity_id: "protein.P0AEB5"
entity_type: "protein"
name: "ynaI"
source_database: "UniProt"
source_id: "P0AEB5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22874652}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22874652}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynaI b1330 JW1323"
---

# ynaI

`protein.P0AEB5`

## Static

- Type: `protein`
- Source: `UniProt:P0AEB5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22874652}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22874652}.

## Enriched Summary

FUNCTION: Mechanosensitive channel that protects cells against hypoosmotic stress when highly overexpressed. {ECO:0000269|PubMed:22874652}.

## Biological Role

Component of small conductance mechanosensitive channel YnaI (complex.ecocyc.CPLX0-7982).

## Annotation

FUNCTION: Mechanosensitive channel that protects cells against hypoosmotic stress when highly overexpressed. {ECO:0000269|PubMed:22874652}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7982|complex.ecocyc.CPLX0-7982]] `EcoCyc` `database` - EcoCyc component coefficient=7 | EcoCyc protcplxs.col coefficient=7

## Incoming Edges (1)

- `encodes` <-- [[gene.b1330|gene.b1330]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEB5`
- `KEGG:ecj:JW1323;eco:b1330;ecoc:C3026_07790;`
- `GeneID:75171457;945898;`
- `GO:GO:0005216; GO:0005886; GO:0008381; GO:0042802; GO:0071470`

## Notes

Low conductance mechanosensitive channel YnaI
