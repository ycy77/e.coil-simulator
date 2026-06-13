---
entity_id: "protein.P0AEU3"
entity_type: "protein"
name: "hisM"
source_database: "UniProt"
source_id: "P0AEU3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisM b2307 JW2304"
---

# hisM

`protein.P0AEU3`

## Static

- Type: `protein`
- Source: `UniProt:P0AEU3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport. Is also part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000250|UniProtKB:P0A2I7}. HisM is one of two predicted integral membrane subunits of an ATP-dependent uptake system for the basic amino acids lysine, arginine, ornithine and histidine.

## Biological Role

Component of histidine ABC transporter (complex.ecocyc.ABC-14-CPLX), lysine / arginine / ornithine ABC transporter (complex.ecocyc.ABC-3-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport. Is also part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000250|UniProtKB:P0A2I7}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-14-CPLX|complex.ecocyc.ABC-14-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.ABC-3-CPLX|complex.ecocyc.ABC-3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2307|gene.b2307]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEU3`
- `KEGG:ecj:JW2304;eco:b2307;ecoc:C3026_12865;`
- `GeneID:93774867;946790;`
- `GO:GO:0005886; GO:0006865; GO:0016020; GO:0022857; GO:0055052; GO:0089718; GO:1903810`

## Notes

Histidine/lysine/arginine/ornithine transport system permease protein HisM
