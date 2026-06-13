---
entity_id: "protein.P0A6J3"
entity_type: "protein"
name: "cysZ"
source_database: "UniProt"
source_id: "P0A6J3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00468, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00468}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysZ b2413 JW2406"
---

# cysZ

`protein.P0A6J3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6J3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00468, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00468}.

## Enriched Summary

FUNCTION: High affinity, high specificity proton-dependent sulfate transporter, which mediates sulfate uptake. Provides the sulfur source for the cysteine synthesis pathway. Does not transport thiosulfate. {ECO:0000269|PubMed:24657232}. CysZ is a high affinity, high specificity sulfate transporter which mediates sulfate uptake for the purpose of cysteine synthesis . CysZ interacts with sulfate, sulfite, sulfide and cysteine but does not interact with thiosulfate. CysZ mediates sulfate uptake into whole cells and proteoliposomes. CysZ mediated sulfate uptake is inhibited by sulfite. CysZ is a sulfate:proton symporter but the exact stoichiometry of the transport reaction is not known . A cysZ mutant is deficient in sulfate assimilation .

## Biological Role

Catalyzes sulfate:proton symport (reaction.ecocyc.TRANS-RXN0-586). Transports Sulfate (molecule.C00059), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: High affinity, high specificity proton-dependent sulfate transporter, which mediates sulfate uptake. Provides the sulfur source for the cysteine synthesis pathway. Does not transport thiosulfate. {ECO:0000269|PubMed:24657232}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-586|reaction.ecocyc.TRANS-RXN0-586]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00059|molecule.C00059]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2413|gene.b2413]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6J3`
- `KEGG:ecj:JW2406;eco:b2413;ecoc:C3026_13415;`
- `GeneID:93774718;946875;`
- `GO:GO:0000103; GO:0005886; GO:0009675; GO:0015116; GO:0019344; GO:1902358`

## Notes

Sulfate transporter CysZ
