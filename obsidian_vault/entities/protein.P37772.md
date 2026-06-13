---
entity_id: "protein.P37772"
entity_type: "protein"
name: "yjfF"
source_database: "UniProt"
source_id: "P37772"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjfF b4231 JW5754"
---

# yjfF

`protein.P37772`

## Static

- Type: `protein`
- Source: `UniProt:P37772`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305, ECO:0000305|PubMed:19744923}. Sequence analysis suggests that YjfF is the integral membrane protein of an ATP-binding cassette (ABC) transporter .

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

- `encodes` <-- [[gene.b4231|gene.b4231]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37772`
- `KEGG:ecj:JW5754;eco:b4231;ecoc:C3026_22840;`
- `GeneID:93777594;948754;`
- `GO:GO:0005886; GO:0022857; GO:0055052; GO:0140271`

## Notes

Inner membrane ABC transporter permease protein YjfF
