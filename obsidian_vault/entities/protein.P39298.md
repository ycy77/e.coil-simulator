---
entity_id: "protein.P39298"
entity_type: "protein"
name: "yjfP"
source_database: "UniProt"
source_id: "P39298"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjfP b4190 JW4148"
---

# yjfP

`protein.P39298`

## Static

- Type: `protein`
- Source: `UniProt:P39298`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Displays esterase activity toward palmitoyl-CoA and pNP-butyrate. {ECO:0000269|PubMed:15808744}.

## Biological Role

Component of carboxylesterase (complex.ecocyc.CPLX0-8214).

## Annotation

FUNCTION: Displays esterase activity toward palmitoyl-CoA and pNP-butyrate. {ECO:0000269|PubMed:15808744}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8214|complex.ecocyc.CPLX0-8214]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4190|gene.b4190]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39298`
- `KEGG:ecj:JW4148;eco:b4190;ecoc:C3026_22635;`
- `GeneID:948707;`
- `GO:GO:0006508; GO:0008236; GO:0016787; GO:0034338; GO:0042803`
- `EC:3.1.-.-`

## Notes

Esterase YjfP (EC 3.1.-.-)
