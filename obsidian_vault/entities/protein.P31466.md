---
entity_id: "protein.P31466"
entity_type: "protein"
name: "adeP"
source_database: "UniProt"
source_id: "P31466"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "adeP purP yieG b3714 JW3692"
---

# adeP

`protein.P31466`

## Static

- Type: `protein`
- Source: `UniProt:P31466`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}.

## Enriched Summary

FUNCTION: High-affinity transporter for adenine. {ECO:0000269|PubMed:24214977, ECO:0000269|PubMed:6198438, ECO:0000269|PubMed:8165228}. AdeP (formerly PurP) functions in energized high-affinity adenine uptake in Escherichia coli. The process requires the metabolic removal of transported adenine, which prevents the accumulation of adenine inside the cell. There is also a non-energized low-affinity adenine uptake process in an adeP deletion mutant, suggesting the existence of another independent system . Cloned and overexpressed AdeP transports adenine but not guanine, hypoxanthine, xanthine, uric acid or uracil . AdeP is a member of the nucleobase:cation symporter 2 (NCS2) family of transporters . adeP: adenine specific permease purP: purine permease

## Biological Role

Catalyzes adenine:proton symport (reaction.ecocyc.TRANS-RXN0-447). Transports Adenine (molecule.C00147), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: High-affinity transporter for adenine. {ECO:0000269|PubMed:24214977, ECO:0000269|PubMed:6198438, ECO:0000269|PubMed:8165228}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-447|reaction.ecocyc.TRANS-RXN0-447]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3714|gene.b3714]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31466`
- `KEGG:ecj:JW3692;eco:b3714;ecoc:C3026_20135;`
- `GeneID:948224;`
- `GO:GO:0005886; GO:0015207; GO:0015295; GO:0015853`

## Notes

Adenine permease AdeP
