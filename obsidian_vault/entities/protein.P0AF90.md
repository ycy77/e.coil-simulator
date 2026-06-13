---
entity_id: "protein.P0AF90"
entity_type: "protein"
name: "rraB"
source_database: "UniProt"
source_id: "P0AF90"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01888}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rraB yjgD b4255 JW4212"
---

# rraB

`protein.P0AF90`

## Static

- Type: `protein`
- Source: `UniProt:P0AF90`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01888}.

## Enriched Summary

FUNCTION: Globally modulates RNA abundance by binding to RNase E (Rne) and regulating its endonucleolytic activity. Can modulate Rne action in a substrate-dependent manner by altering the composition of the degradosome. {ECO:0000255|HAMAP-Rule:MF_01888, ECO:0000269|PubMed:16771842, ECO:0000269|PubMed:18510556}.

## Biological Role

Component of ribonuclease E inhibitor protein B (complex.ecocyc.CPLX0-8096).

## Annotation

FUNCTION: Globally modulates RNA abundance by binding to RNase E (Rne) and regulating its endonucleolytic activity. Can modulate Rne action in a substrate-dependent manner by altering the composition of the degradosome. {ECO:0000255|HAMAP-Rule:MF_01888, ECO:0000269|PubMed:16771842, ECO:0000269|PubMed:18510556}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8096|complex.ecocyc.CPLX0-8096]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4255|gene.b4255]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF90`
- `KEGG:ecj:JW4212;eco:b4255;ecoc:C3026_22955;`
- `GeneID:93777567;948773;`
- `GO:GO:0005829; GO:0006402; GO:0008428; GO:0019899; GO:0042803; GO:0060698; GO:0060699`

## Notes

Regulator of ribonuclease activity B
