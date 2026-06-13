---
entity_id: "protein.P0ACK8"
entity_type: "protein"
name: "fucR"
source_database: "UniProt"
source_id: "P0ACK8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fucR b2805 JW2776"
---

# fucR

`protein.P0ACK8`

## Static

- Type: `protein`
- Source: `UniProt:P0ACK8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional activator of the fuc operon.

## Biological Role

Component of FucR-L-fuculose-1-phosphate DNA-binding transcriptional activator (complex.ecocyc.CPLX0-7650).

## Annotation

FUNCTION: Transcriptional activator of the fuc operon.

## Outgoing Edges (3)

- `activates` --> [[gene.b2799|gene.b2799]] `RegulonDB` `S` - regulator=FucR; target=fucO; function=+
- `activates` --> [[gene.b2800|gene.b2800]] `RegulonDB` `S` - regulator=FucR; target=fucA; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7650|complex.ecocyc.CPLX0-7650]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b2805|gene.b2805]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACK8`
- `KEGG:ecj:JW2776;eco:b2805;ecoc:C3026_15420;`
- `GeneID:93779193;946905;`
- `GO:GO:0000987; GO:0006004; GO:0006355; GO:0043468; GO:0098531`

## Notes

L-fucose operon activator
