---
entity_id: "protein.P18196"
entity_type: "protein"
name: "minC"
source_database: "UniProt"
source_id: "P18196"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "minC b1176 JW1165"
---

# minC

`protein.P18196`

## Static

- Type: `protein`
- Source: `UniProt:P18196`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Cell division inhibitor that blocks the formation of polar Z ring septums. Rapidly oscillates between the poles of the cell to destabilize FtsZ filaments that have formed before they mature into polar Z rings. Prevents FtsZ polymerization. {ECO:0000269|PubMed:22380631}.

## Biological Role

Component of Z-ring inhibitor complex MinCD (complex.ecocyc.CPLX0-8188), Z-ring positioning protein MinC (complex.ecocyc.CPLX0-8196).

## Annotation

FUNCTION: Cell division inhibitor that blocks the formation of polar Z ring septums. Rapidly oscillates between the poles of the cell to destabilize FtsZ filaments that have formed before they mature into polar Z rings. Prevents FtsZ polymerization. {ECO:0000269|PubMed:22380631}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8188|complex.ecocyc.CPLX0-8188]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8196|complex.ecocyc.CPLX0-8196]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1176|gene.b1176]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18196`
- `KEGG:ecj:JW1165;eco:b1176;ecoc:C3026_06930;`
- `GeneID:945744;`
- `GO:GO:0000902; GO:0000918; GO:0004857; GO:0005829; GO:0007105; GO:0042802; GO:0051302; GO:0060187; GO:1901891`

## Notes

Septum site-determining protein MinC
