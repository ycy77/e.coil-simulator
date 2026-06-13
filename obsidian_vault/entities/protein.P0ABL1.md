---
entity_id: "protein.P0ABL1"
entity_type: "protein"
name: "nrfB"
source_database: "UniProt"
source_id: "P0ABL1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrfB yjcI b4071 JW4032"
---

# nrfB

`protein.P0ABL1`

## Static

- Type: `protein`
- Source: `UniProt:P0ABL1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Plays a role in nitrite reduction.

## Biological Role

Component of periplasmic nitrite reductase penta-heme c-type cytochrome (complex.ecocyc.CPLX0-12841), periplasmic nitrite reductase NrfAB (complex.ecocyc.NRFMULTI-CPLX).

## Annotation

FUNCTION: Plays a role in nitrite reduction.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12841|complex.ecocyc.CPLX0-12841]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.NRFMULTI-CPLX|complex.ecocyc.NRFMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4071|gene.b4071]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABL1`
- `KEGG:ecj:JW4032;eco:b4071;ecoc:C3026_22005;`
- `GeneID:93777758;948573;`
- `GO:GO:0009055; GO:0016491; GO:0019645; GO:0020037; GO:0030288; GO:0042279; GO:0046872`

## Notes

Cytochrome c-type protein NrfB
