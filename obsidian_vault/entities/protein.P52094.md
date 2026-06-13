---
entity_id: "protein.P52094"
entity_type: "protein"
name: "hisQ"
source_database: "UniProt"
source_id: "P52094"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisQ b2308 JW2305"
---

# hisQ

`protein.P52094`

## Static

- Type: `protein`
- Source: `UniProt:P52094`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport. Is also part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000250|UniProtKB:P0A2I9}. HisQ is one of two predicted integral membrane subunits of an ATP-dependent uptake system for the basic amino acids lysine, arginine, ornithine and histidine.

## Biological Role

Component of histidine ABC transporter (complex.ecocyc.ABC-14-CPLX), lysine / arginine / ornithine ABC transporter (complex.ecocyc.ABC-3-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport. Is also part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000250|UniProtKB:P0A2I9}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-14-CPLX|complex.ecocyc.ABC-14-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.ABC-3-CPLX|complex.ecocyc.ABC-3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2308|gene.b2308]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52094`
- `KEGG:ecj:JW2305;eco:b2308;ecoc:C3026_12870;`
- `GeneID:947235;`
- `GO:GO:0005291; GO:0005886; GO:0016020; GO:0055052; GO:0089709; GO:0089718; GO:1903810`

## Notes

Histidine/lysine/arginine/ornithine transport system permease protein HisQ
