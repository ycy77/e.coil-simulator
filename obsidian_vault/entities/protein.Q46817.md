---
entity_id: "protein.Q46817"
entity_type: "protein"
name: "ghxQ"
source_database: "UniProt"
source_id: "Q46817"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:24214977}; Multi-pass membrane protein {ECO:0000269|PubMed:24214977}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ghxQ ygfQ ygfR b4464 JW5467"
---

# ghxQ

`protein.Q46817`

## Static

- Type: `protein`
- Source: `UniProt:Q46817`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:24214977}; Multi-pass membrane protein {ECO:0000269|PubMed:24214977}.

## Enriched Summary

FUNCTION: High-affinity transporter for guanine and hypoxanthine. {ECO:0000269|PubMed:24214977}. GhxQ mediates the uptake of guanine and hypoxanthine (but not adenine, xanthine, uric acid nor uracil) when overexpressed in strains (ΔyjcD or ΔpurP) which lack significant background activity; GhxQ transports guanine and hypoxanthine with high affinity . GhxQ is a member of the nucleobase:cation symporter 2 (NCS2) family of transporters . GhxQ is part of a putative purine catablic operon . Expression of ghxQ is significantly induced under acidic growth conditions (pH 5.5 and 4.5) . ghxQ: guanine / hypoxanthine permease Q

## Biological Role

Catalyzes TRANS-RXN0-562 (reaction.ecocyc.TRANS-RXN0-562), TRANS-RXN0-578 (reaction.ecocyc.TRANS-RXN0-578). Transports Guanine (molecule.C00242), Hypoxanthine (molecule.C00262), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: High-affinity transporter for guanine and hypoxanthine. {ECO:0000269|PubMed:24214977}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-562|reaction.ecocyc.TRANS-RXN0-562]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-578|reaction.ecocyc.TRANS-RXN0-578]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4464|gene.b4464]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46817`
- `KEGG:ecj:JW5467;eco:b4464;ecoc:C3026_15815;`
- `GeneID:2847748;75172984;75205279;`
- `GO:GO:0005886; GO:0015208; GO:0016020; GO:0035344; GO:0098710`

## Notes

Guanine/hypoxanthine permease GhxQ
