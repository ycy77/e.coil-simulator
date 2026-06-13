---
entity_id: "protein.P31549"
entity_type: "protein"
name: "thiP"
source_database: "UniProt"
source_id: "P31549"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiP yabK b0067 JW0066"
---

# thiP

`protein.P31549`

## Static

- Type: `protein`
- Source: `UniProt:P31549`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ThiBPQ involved in thiamine import (PubMed:12175925). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:12175925, ECO:0000305}. ThiP is the predicted inner membrane permease of an ATP-dependent thiamine uptake system

## Biological Role

Component of thiamine ABC transporter (complex.ecocyc.ABC-32-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ThiBPQ involved in thiamine import (PubMed:12175925). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:12175925, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-32-CPLX|complex.ecocyc.ABC-32-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0067|gene.b0067]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31549`
- `KEGG:ecj:JW0066;eco:b0067;`
- `GeneID:944784;`
- `GO:GO:0005886; GO:0015234; GO:0016020; GO:0055052; GO:0071934`

## Notes

Thiamine transport system permease protein ThiP
