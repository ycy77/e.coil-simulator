---
entity_id: "protein.P0A9T8"
entity_type: "protein"
name: "ybbA"
source_database: "UniProt"
source_id: "P0A9T8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybbA b0495 JW0484"
---

# ybbA

`protein.P0A9T8`

## Static

- Type: `protein`
- Source: `UniProt:P0A9T8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized ABC transporter ATP-binding protein YbbA YbbA is the predicted ATP-binding subunit of a putative ATP-binding cassette (ABC) exporter complex . YbbA contains sequence motifs conserved in ATP-binding cassette proteins . YbbA is upregulated in response to exogenous L-threonine; expression of ybbA from a multicopy plasmid increases the resistance of wild-type E. coli to high concentrations of L-threonine .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-61-CPLX).

## Annotation

Uncharacterized ABC transporter ATP-binding protein YbbA

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-61-CPLX|complex.ecocyc.ABC-61-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0495|gene.b0495]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9T8`
- `KEGG:ecj:JW0484;eco:b0495;ecoc:C3026_02435;`
- `GeneID:93776954;945122;`
- `GO:GO:0005524; GO:0016887`

## Notes

Uncharacterized ABC transporter ATP-binding protein YbbA
