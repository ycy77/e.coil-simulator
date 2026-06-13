---
entity_id: "protein.P69488"
entity_type: "protein"
name: "cutA"
source_database: "UniProt"
source_id: "P69488"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:7623666}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cutA cutA1 cycY b4137 JW4097"
---

# cutA

`protein.P69488`

## Static

- Type: `protein`
- Source: `UniProt:P69488`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:7623666}.

## Enriched Summary

FUNCTION: Involved in resistance toward heavy metals. {ECO:0000269|PubMed:7623666}.

## Biological Role

Component of copper binding protein CutA (complex.ecocyc.CPLX0-3938).

## Annotation

FUNCTION: Involved in resistance toward heavy metals. {ECO:0000269|PubMed:7623666}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3938|complex.ecocyc.CPLX0-3938]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b4137|gene.b4137]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69488`
- `KEGG:ecj:JW4097;eco:b4137;ecoc:C3026_22360;`
- `GeneID:93777687;948660;`
- `GO:GO:0005507; GO:0005737; GO:0032991; GO:0046688; GO:0046872`

## Notes

Divalent-cation tolerance protein CutA (C-type cytochrome biogenesis protein CycY)
