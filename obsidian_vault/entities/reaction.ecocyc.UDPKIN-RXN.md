---
entity_id: "reaction.ecocyc.UDPKIN-RXN"
entity_type: "reaction"
name: "UDPKIN-RXN"
source_database: "EcoCyc"
source_id: "UDPKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPKIN-RXN

`reaction.ecocyc.UDPKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP + ATP -> UTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: UDP + ATP -> UTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside diphosphate kinase (complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX), adk (protein.P69441). Substrates: ATP (molecule.C00002), UDP (molecule.C00015). Products: ADP (molecule.C00008), UTP (molecule.C00075).

## Enriched Pathways

- `ecocyc.PWY-7176` UTP and CTP de novo biosynthesis (EcoCyc)

## Annotation

UDP + ATP -> UTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7176` UTP and CTP de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX|complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P69441|protein.P69441]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDPKIN-RXN`

## Notes

UDP + ATP -> UTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
