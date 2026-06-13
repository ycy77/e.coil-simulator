---
entity_id: "protein.P0AFS1"
entity_type: "protein"
name: "lsrD"
source_database: "UniProt"
source_id: "P0AFS1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lsrD ydeZ b1515 JW1508"
---

# lsrD

`protein.P0AFS1`

## Static

- Type: `protein`
- Source: `UniProt:P0AFS1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305|PubMed:15601708}. Based on sequence similarity lsrD is predicted to encode the membrane component of an AI-2 ABC transporter . lsrD is required for growth under optimum growth conditions (rich medium at 37°C), but not under cold conditions (15°C) or in minimal medium .

## Biological Role

Component of Autoinducer-2 ABC transporter (complex.ecocyc.ABC-58-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305|PubMed:15601708}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-58-CPLX|complex.ecocyc.ABC-58-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1515|gene.b1515]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFS1`
- `KEGG:ecj:JW1508;eco:b1515;ecoc:C3026_08760;`
- `GeneID:75202157;946264;`
- `GO:GO:0005886; GO:0009372; GO:0016020; GO:0022857; GO:0055052; GO:1905887`

## Notes

Autoinducer 2 import system permease protein LsrD (AI-2 import system permease protein LsrD)
