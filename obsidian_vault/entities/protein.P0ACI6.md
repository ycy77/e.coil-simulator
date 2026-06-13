---
entity_id: "protein.P0ACI6"
entity_type: "protein"
name: "asnC"
source_database: "UniProt"
source_id: "P0ACI6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "asnC b3743 JW3721"
---

# asnC

`protein.P0ACI6`

## Static

- Type: `protein`
- Source: `UniProt:P0ACI6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Activator of asnA transcription; autogenous regulator of its own transcription; and repressor of the expression of gidA at a post-transcriptional level. {ECO:0000269|PubMed:2836709, ECO:0000269|PubMed:2864330, ECO:0000269|PubMed:3909107}.

## Biological Role

Component of DNA-binding transcriptional dual regulator AsnC (complex.ecocyc.CPLX0-7733).

## Annotation

FUNCTION: Activator of asnA transcription; autogenous regulator of its own transcription; and repressor of the expression of gidA at a post-transcriptional level. {ECO:0000269|PubMed:2836709, ECO:0000269|PubMed:2864330, ECO:0000269|PubMed:3909107}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7733|complex.ecocyc.CPLX0-7733]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3743|gene.b3743]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACI6`
- `KEGG:ecj:JW3721;eco:b3743;ecoc:C3026_20280;`
- `GeneID:86861851;948259;`
- `GO:GO:0003700; GO:0006355; GO:0042802; GO:0043200; GO:0043565; GO:0045892; GO:0045893`

## Notes

Regulatory protein AsnC
