---
entity_id: "protein.P07109"
entity_type: "protein"
name: "hisP"
source_database: "UniProt"
source_id: "P07109"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P02915}; Peripheral membrane protein {ECO:0000250|UniProtKB:P02915}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisP b2306 JW2303"
---

# hisP

`protein.P07109`

## Static

- Type: `protein`
- Source: `UniProt:P07109`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P02915}; Peripheral membrane protein {ECO:0000250|UniProtKB:P02915}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport. Is also part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Shows ATPase activity. Responsible for energy coupling to the transport system. {ECO:0000250|UniProtKB:P02915}. HisP is the predicted ATP binding subunit of an ATP-dependent uptake system for the basic amino acids lysine, arginine, ornithine and histidine. HisP contains signature motifs conserved in ATP-binding cassette (ABC) domains

## Biological Role

Component of histidine ABC transporter (complex.ecocyc.ABC-14-CPLX), lysine / arginine / ornithine ABC transporter (complex.ecocyc.ABC-3-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport. Is also part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Shows ATPase activity. Responsible for energy coupling to the transport system. {ECO:0000250|UniProtKB:P02915}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-14-CPLX|complex.ecocyc.ABC-14-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.ABC-3-CPLX|complex.ecocyc.ABC-3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2306|gene.b2306]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07109`
- `KEGG:ecj:JW2303;eco:b2306;ecoc:C3026_12860;`
- `GeneID:946789;`
- `GO:GO:0005291; GO:0005524; GO:0005886; GO:0015426; GO:0016020; GO:0016887; GO:0042626; GO:0055052; GO:0089709; GO:0089718; GO:1903810`
- `EC:7.4.2.1`

## Notes

Histidine/lysine/arginine/ornithine transport ATP-binding protein HisP (EC 7.4.2.1)
