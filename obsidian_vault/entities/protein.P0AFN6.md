---
entity_id: "protein.P0AFN6"
entity_type: "protein"
name: "yadH"
source_database: "UniProt"
source_id: "P0AFN6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yadH b0128 JW0124"
---

# yadH

`protein.P0AFN6`

## Static

- Type: `protein`
- Source: `UniProt:P0AFN6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

Inner membrane transport permease YadH YadH is the predicted membrane-spanning subunit of a putative ATP-binding cassette (ABC) exporter complex .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-21-CPLX).

## Annotation

Inner membrane transport permease YadH

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-21-CPLX|complex.ecocyc.ABC-21-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0128|gene.b0128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFN6`
- `KEGG:ecj:JW0124;eco:b0128;ecoc:C3026_00545;`
- `GeneID:93777308;944836;`
- `GO:GO:0005886; GO:0043190; GO:0140359`

## Notes

Inner membrane transport permease YadH
