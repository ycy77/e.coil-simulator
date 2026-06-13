---
entity_id: "protein.P31440"
entity_type: "protein"
name: "adeQ"
source_database: "UniProt"
source_id: "P31440"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "adeQ yicO b3664 JW5636"
---

# adeQ

`protein.P31440`

## Static

- Type: `protein`
- Source: `UniProt:P31440`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}.

## Enriched Summary

FUNCTION: High-affinity transporter for adenine. {ECO:0000269|PubMed:24214977}. AdeQ is a high-affinity adenine transporter in E. coli K-12. Cloned and overexpressed AdeQ transports labelled adenine but not guanine, hypoxanthine, xanthine, uric acid or uracil in an E. coli ΔpurP strain . AdeQ is a member of the nucleobase:cation symporter 2 (NCS2) family of transporters . Transcription is regulated by BaeR, which plays a role in novobiocin and deoxycholate resistance . adeQ: adenine permease

## Biological Role

Catalyzes transport of adenine (reaction.ecocyc.TRANS-RXN0-577).

## Annotation

FUNCTION: High-affinity transporter for adenine. {ECO:0000269|PubMed:24214977}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-577|reaction.ecocyc.TRANS-RXN0-577]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3664|gene.b3664]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31440`
- `KEGG:ecj:JW5636;eco:b3664;`
- `GeneID:948174;`
- `GO:GO:0005886; GO:0015207; GO:0015853`

## Notes

Adenine permease AdeQ
