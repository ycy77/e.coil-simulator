---
entity_id: "protein.P77504"
entity_type: "protein"
name: "ybbP"
source_database: "UniProt"
source_id: "P77504"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybbP b0496 JW0485"
---

# ybbP

`protein.P77504`

## Static

- Type: `protein`
- Source: `UniProt:P77504`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

Uncharacterized ABC transporter permease YbbP YbbP is the predicted membrane-spanning subunit of a putative ATP-binding cassette (ABC) exporter complex .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-61-CPLX).

## Annotation

Uncharacterized ABC transporter permease YbbP

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-61-CPLX|complex.ecocyc.ABC-61-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0496|gene.b0496]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77504`
- `KEGG:ecj:JW0485;eco:b0496;ecoc:C3026_02440;`
- `GeneID:945118;`
- `GO:GO:0005886`

## Notes

Uncharacterized ABC transporter permease YbbP
