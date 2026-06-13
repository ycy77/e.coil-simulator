---
entity_id: "protein.P37005"
entity_type: "protein"
name: "lasT"
source_database: "UniProt"
source_id: "P37005"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lasT yjtD b4403 JW4366"
---

# lasT

`protein.P37005`

## Static

- Type: `protein`
- Source: `UniProt:P37005`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized tRNA/rRNA methyltransferase LasT (EC 2.1.1.-) YjtD belongs to the SPOUT superfamily of methyltransferases . YjtD shows no methyltransferase activity with certain tRNA substrates . YjtD is a dimer in solution .

## Biological Role

Component of putative tRNA/rRNA methyltransferase YjtD (complex.ecocyc.CPLX0-7422).

## Annotation

Uncharacterized tRNA/rRNA methyltransferase LasT (EC 2.1.1.-)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7422|complex.ecocyc.CPLX0-7422]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4403|gene.b4403]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37005`
- `KEGG:ecj:JW4366;eco:b4403;ecoc:C3026_23790;`
- `GeneID:948924;`
- `GO:GO:0002128; GO:0003723; GO:0005829; GO:0008173; GO:0042803`
- `EC:2.1.1.-`

## Notes

Uncharacterized tRNA/rRNA methyltransferase LasT (EC 2.1.1.-)
