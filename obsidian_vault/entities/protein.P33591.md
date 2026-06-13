---
entity_id: "protein.P33591"
entity_type: "protein"
name: "nikB"
source_database: "UniProt"
source_id: "P33591"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nikB b3477 JW3442"
---

# nikB

`protein.P33591`

## Static

- Type: `protein`
- Source: `UniProt:P33591`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in a nickel transport system, probably translocates nickel through the bacterial inner membrane. NikB is one of two predicted inner membrane subunits of a high affinity uptake system for Ni2+; NikB contains six potential transmembrane α-helices .

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

- `encodes` <-- [[gene.b3477|gene.b3477]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33591`
- `KEGG:ecj:JW3442;eco:b3477;ecoc:C3026_18830;`
- `GeneID:93778514;947986;`
- `GO:GO:0005886; GO:0015099; GO:0016020; GO:0016151; GO:0055052; GO:0071916; GO:0098716`

## Notes

Nickel transport system permease protein NikB
