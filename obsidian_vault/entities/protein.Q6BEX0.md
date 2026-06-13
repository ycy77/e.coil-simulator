---
entity_id: "protein.Q6BEX0"
entity_type: "protein"
name: "ytfR"
source_database: "UniProt"
source_id: "Q6BEX0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ytfR ytfS b4485 JW5752"
---

# ytfR

`protein.Q6BEX0`

## Static

- Type: `protein`
- Source: `UniProt:Q6BEX0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Responsible for energy coupling to the transport system (Probable). {ECO:0000305, ECO:0000305|PubMed:19744923}. Sequence analysis suggests that YtfR is tthe ATP binding protein of an ATP-binding cassette (ABC) transporter .

## Biological Role

Component of galactofuranose ABC transporter (complex.ecocyc.ABC-46-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Responsible for energy coupling to the transport system (Probable). {ECO:0000305, ECO:0000305|PubMed:19744923}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-46-CPLX|complex.ecocyc.ABC-46-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4485|gene.b4485]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q6BEX0`
- `KEGG:ecj:JW5752;eco:b4485;ecoc:C3026_22830;`
- `GeneID:2847725;`
- `GO:GO:0005524; GO:0005886; GO:0016887; GO:0022857; GO:0042626; GO:0055052; GO:0103116; GO:0140271`
- `EC:7.5.2.9`

## Notes

Galactofuranose transporter ATP-binding protein YtfR (EC 7.5.2.9)
