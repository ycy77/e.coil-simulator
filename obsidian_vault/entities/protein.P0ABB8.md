---
entity_id: "protein.P0ABB8"
entity_type: "protein"
name: "mgtA"
source_database: "UniProt"
source_id: "P0ABB8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:40550995}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mgtA corB mgt b4242 JW4201"
---

# mgtA

`protein.P0ABB8`

## Static

- Type: `protein`
- Source: `UniProt:P0ABB8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:40550995}.

## Enriched Summary

FUNCTION: Mediates magnesium influx to the cytosol (PubMed:40550995). Essential for bacterial growth during magnesium depletion (PubMed:40550995). {ECO:0000269|PubMed:40550995}.

## Biological Role

Component of Mg2+ transporting P-type ATPase (complex.ecocyc.CPLX0-13311).

## Annotation

FUNCTION: Mediates magnesium influx to the cytosol (PubMed:40550995). Essential for bacterial growth during magnesium depletion (PubMed:40550995). {ECO:0000269|PubMed:40550995}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13311|complex.ecocyc.CPLX0-13311]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4242|gene.b4242]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABB8`
- `KEGG:ecj:JW4201;eco:b4242;ecoc:C3026_22895;`
- `GeneID:948778;`
- `GO:GO:0005524; GO:0005886; GO:0015444; GO:0015662; GO:0016887; GO:0019829; GO:0046872; GO:0071286; GO:1903830`
- `EC:7.2.2.14`

## Notes

Magnesium-transporting ATPase, P-type 1 (EC 7.2.2.14) (Mg(2+) transport ATPase, P-type 1)
