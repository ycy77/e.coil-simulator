---
entity_id: "reaction.ecocyc.DGDPKIN-RXN"
entity_type: "reaction"
name: "DGDPKIN-RXN"
source_database: "EcoCyc"
source_id: "DGDPKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DGDPKIN-RXN

`reaction.ecocyc.DGDPKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DGDPKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DGDP + ATP -> DGTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DGDP + ATP -> DGTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside diphosphate kinase (complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX), adk (protein.P69441). Substrates: ATP (molecule.C00002), dGDP (molecule.C00361). Products: ADP (molecule.C00008), dGTP (molecule.C00286).

## Enriched Pathways

- `ecocyc.PWY-7222` guanosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Annotation

DGDP + ATP -> DGTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7222` guanosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX|complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P69441|protein.P69441]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00361|molecule.C00361]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DGDPKIN-RXN`

## Notes

DGDP + ATP -> DGTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
