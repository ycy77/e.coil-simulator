---
entity_id: "protein.P02924"
entity_type: "protein"
name: "araF"
source_database: "UniProt"
source_id: "P02924"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "araF b1901 JW1889"
---

# araF

`protein.P02924`

## Static

- Type: `protein`
- Source: `UniProt:P02924`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Involved in the high-affinity L-arabinose membrane transport system. Binds with high affinity to arabinose, but can also bind D-galactose (approximately 2-fold reduction) and D-fucose (approximately 40-fold reduction). araF encodes the periplasmic binding protein of the high-affinity arabinose transport system. Purified AraF binds L-arabinose

## Biological Role

Component of arabinose ABC transporter (complex.ecocyc.ABC-2-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Involved in the high-affinity L-arabinose membrane transport system. Binds with high affinity to arabinose, but can also bind D-galactose (approximately 2-fold reduction) and D-fucose (approximately 40-fold reduction).

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-2-CPLX|complex.ecocyc.ABC-2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1901|gene.b1901]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02924`
- `KEGG:ecj:JW1889;eco:b1901;ecoc:C3026_10790;`
- `GeneID:75202696;946409;`
- `GO:GO:0015407; GO:0016020; GO:0030246; GO:0030288; GO:0042882; GO:0048029; GO:0055052`

## Notes

L-arabinose-binding periplasmic protein (ABP)
