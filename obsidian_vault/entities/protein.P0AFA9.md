---
entity_id: "protein.P0AFA9"
entity_type: "protein"
name: "nikC"
source_database: "UniProt"
source_id: "P0AFA9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nikC b3478 JW3443"
---

# nikC

`protein.P0AFA9`

## Static

- Type: `protein`
- Source: `UniProt:P0AFA9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in a nickel transport system, probably translocates nickel through the bacterial inner membrane. NikC is one of two predicted inner membrane subunits of a high affinity uptake system for Ni2+; NikC contains six potential transmembrane α-helices .

## Biological Role

Component of Ni(2+) ABC transporter (complex.ecocyc.ABC-20-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Involved in a nickel transport system, probably translocates nickel through the bacterial inner membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-20-CPLX|complex.ecocyc.ABC-20-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3478|gene.b3478]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFA9`
- `KEGG:ecj:JW3443;eco:b3478;ecoc:C3026_18835;`
- `GeneID:93778513;947990;`
- `GO:GO:0005886; GO:0015099; GO:0016020; GO:0016151; GO:0055052; GO:0071916; GO:0098716`

## Notes

Nickel transport system permease protein NikC
