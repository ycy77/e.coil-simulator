---
entity_id: "protein.P37028"
entity_type: "protein"
name: "btuF"
source_database: "UniProt"
source_id: "P37028"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_01000, ECO:0000269|PubMed:11790740}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "btuF yadT b0158 JW0154"
---

# btuF

`protein.P37028`

## Static

- Type: `protein`
- Source: `UniProt:P37028`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_01000, ECO:0000269|PubMed:11790740}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex BtuCDF involved in vitamin B12 import. Binds vitamin B12 and delivers it to the periplasmic surface of BtuC. {ECO:0000255|HAMAP-Rule:MF_01000, ECO:0000269|PubMed:11790740}. BtuF is the periplasmic binding protein of an ATP-dependent vitamin B12 uptake system. Purified BtuF binds cyanocobalamin with high affinity (Kd approx 15 nM) ; purified BtuF binds cobinamide with high affinity (Kd = 40 nM) Purified BtuF contains two structurally similar lobes connected by a single linking α-helix; Vitamin B12 binds in a deep cleft between the two lobes

## Biological Role

Component of vitamin B12 ABC transporter (complex.ecocyc.ABC-5-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex BtuCDF involved in vitamin B12 import. Binds vitamin B12 and delivers it to the periplasmic surface of BtuC. {ECO:0000255|HAMAP-Rule:MF_01000, ECO:0000269|PubMed:11790740}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-5-CPLX|complex.ecocyc.ABC-5-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0158|gene.b0158]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37028`
- `KEGG:ecj:JW0154;eco:b0158;ecoc:C3026_00720;`
- `GeneID:93777268;947574;`
- `GO:GO:0015889; GO:0016020; GO:0030288; GO:0031419; GO:0042597; GO:1990191`

## Notes

Vitamin B12-binding protein
