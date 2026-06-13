---
entity_id: "reaction.ecocyc.CDPKIN-RXN"
entity_type: "reaction"
name: "CDPKIN-RXN"
source_database: "EcoCyc"
source_id: "CDPKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CDPKIN-RXN

`reaction.ecocyc.CDPKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CDPKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CDP + ATP -> CTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CDP + ATP -> CTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside diphosphate kinase (complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX), adk (protein.P69441). Substrates: ATP (molecule.C00002), CDP (molecule.C00112). Products: ADP (molecule.C00008), CTP (molecule.C00063).

## Enriched Pathways

- `ecocyc.PWY-7205` CMP phosphorylation (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Annotation

CDP + ATP -> CTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7205` CMP phosphorylation (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX|complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P69441|protein.P69441]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00112|molecule.C00112]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CDPKIN-RXN`

## Notes

CDP + ATP -> CTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
