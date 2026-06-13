---
entity_id: "protein.P77509"
entity_type: "protein"
name: "yphE"
source_database: "UniProt"
source_id: "P77509"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yphE b2547 JW2531"
---

# yphE

`protein.P77509`

## Static

- Type: `protein`
- Source: `UniProt:P77509`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably part of a binding-protein-dependent transport system YphDEF. Probably responsible for energy coupling to the transport system. YphE is predicted to be the ATP-binding subunit of a putative ABC transporter .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-60-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Probably part of a binding-protein-dependent transport system YphDEF. Probably responsible for energy coupling to the transport system.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-60-CPLX|complex.ecocyc.ABC-60-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2547|gene.b2547]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77509`
- `KEGG:ecj:JW2531;eco:b2547;ecoc:C3026_14105;`
- `GeneID:948990;`
- `GO:GO:0005524; GO:0005886; GO:0016020; GO:0016887; GO:0022857; GO:0043190; GO:0055052; GO:0055085`

## Notes

Uncharacterized ABC transporter ATP-binding protein YphE
