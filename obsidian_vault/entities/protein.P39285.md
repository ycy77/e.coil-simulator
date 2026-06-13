---
entity_id: "protein.P39285"
entity_type: "protein"
name: "mscM"
source_database: "UniProt"
source_id: "P39285"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22874652}; Multi-pass membrane protein {ECO:0000269|PubMed:22874652}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mscM yjeP b4159 JW4120"
---

# mscM

`protein.P39285`

## Static

- Type: `protein`
- Source: `UniProt:P39285`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22874652}; Multi-pass membrane protein {ECO:0000269|PubMed:22874652}.

## Enriched Summary

FUNCTION: Mechanosensitive channel that protects cells against hypoosmotic stress when highly overexpressed. Gates spontaneously in response to increased membrane tension. {ECO:0000269|PubMed:22874652}.

## Biological Role

Component of miniconductance mechanosensitive channel MscM (complex.ecocyc.CPLX0-7985).

## Annotation

FUNCTION: Mechanosensitive channel that protects cells against hypoosmotic stress when highly overexpressed. Gates spontaneously in response to increased membrane tension. {ECO:0000269|PubMed:22874652}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7985|complex.ecocyc.CPLX0-7985]] `EcoCyc` `database` - EcoCyc component coefficient=7 | EcoCyc protcplxs.col coefficient=7

## Incoming Edges (1)

- `encodes` <-- [[gene.b4159|gene.b4159]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39285`
- `KEGG:ecj:JW4120;eco:b4159;ecoc:C3026_22480;`
- `GeneID:948676;`
- `GO:GO:0005886; GO:0008381; GO:0071470`

## Notes

Miniconductance mechanosensitive channel MscM
