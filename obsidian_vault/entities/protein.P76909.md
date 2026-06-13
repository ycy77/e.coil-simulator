---
entity_id: "protein.P76909"
entity_type: "protein"
name: "ynjD"
source_database: "UniProt"
source_id: "P76909"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynjD b1756 JW5286"
---

# ynjD

`protein.P76909`

## Static

- Type: `protein`
- Source: `UniProt:P76909`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably part of a binding-protein-dependent transport system YnjCD. Probably responsible for energy coupling to the transport system. YnjD is predicted to be the ATP-binding component of a putative ATP dependent transporter complex .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-48-CPLX).

## Annotation

FUNCTION: Probably part of a binding-protein-dependent transport system YnjCD. Probably responsible for energy coupling to the transport system.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-48-CPLX|complex.ecocyc.ABC-48-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1756|gene.b1756]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76909`
- `KEGG:ecj:JW5286;eco:b1756;ecoc:C3026_10025;`
- `GeneID:944965;`
- `GO:GO:0005524; GO:0005886; GO:0015417; GO:0016020; GO:0016887; GO:0043190; GO:0055052; GO:0055085`

## Notes

Uncharacterized ABC transporter ATP-binding protein YnjD
