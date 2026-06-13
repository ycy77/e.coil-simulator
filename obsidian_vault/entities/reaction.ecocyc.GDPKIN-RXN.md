---
entity_id: "reaction.ecocyc.GDPKIN-RXN"
entity_type: "reaction"
name: "GDPKIN-RXN"
source_database: "EcoCyc"
source_id: "GDPKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GDPKIN-RXN

`reaction.ecocyc.GDPKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GDPKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GDP + ATP -> GTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GDP + ATP -> GTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside diphosphate kinase (complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX), adk (protein.P69441). Substrates: ATP (molecule.C00002), GDP (molecule.C00035). Products: ADP (molecule.C00008), GTP (molecule.C00044).

## Enriched Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)
- `ecocyc.PWY-7221` guanosine ribonucleotides de novo biosynthesis (EcoCyc)

## Annotation

GDP + ATP -> GTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)
- `ecocyc.PWY-7221` guanosine ribonucleotides de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX|complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P69441|protein.P69441]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GDPKIN-RXN`

## Notes

GDP + ATP -> GTP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
