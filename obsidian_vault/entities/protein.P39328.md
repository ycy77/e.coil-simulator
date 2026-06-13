---
entity_id: "protein.P39328"
entity_type: "protein"
name: "ytfT"
source_database: "UniProt"
source_id: "P39328"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ytfT b4230 JW5753"
---

# ytfT

`protein.P39328`

## Static

- Type: `protein`
- Source: `UniProt:P39328`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305, ECO:0000305|PubMed:19744923}. Sequence analysis suggests that YtfT is the integral membrane protein of an ATP-binding cassette (ABC) transporter .

## Biological Role

Component of galactofuranose ABC transporter (complex.ecocyc.ABC-46-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305, ECO:0000305|PubMed:19744923}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-46-CPLX|complex.ecocyc.ABC-46-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4230|gene.b4230]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39328`
- `KEGG:ecj:JW5753;eco:b4230;`
- `GeneID:948743;`
- `GO:GO:0005886; GO:0022857; GO:0055052; GO:0140271`

## Notes

Galactofuranose transporter permease protein YtfT
