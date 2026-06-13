---
entity_id: "reaction.ecocyc.ETHAMLY-RXN"
entity_type: "reaction"
name: "ETHAMLY-RXN"
source_database: "EcoCyc"
source_id: "ETHAMLY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ETHAMLY-RXN

`reaction.ecocyc.ETHAMLY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ETHAMLY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is used in ethanolamine utilization. EcoCyc reaction equation: ETHANOL-AMINE -> AMMONIUM + ACETALD; direction=LEFT-TO-RIGHT. This reaction is used in ethanolamine utilization.

## Biological Role

Catalyzed by ethanolamine ammonia-lyase (complex.ecocyc.ETHAMLY-CPLX). Substrates: Ethanolamine (molecule.C00189). Products: Acetaldehyde (molecule.C00084), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Annotation

This reaction is used in ethanolamine utilization.

## Pathways

- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.ETHAMLY-CPLX|complex.ecocyc.ETHAMLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00189|molecule.C00189]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C02823|molecule.C02823]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C03194|molecule.C03194]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06453|molecule.C06453]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C08230|molecule.C08230]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1258|molecule.ecocyc.CPD0-1258]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1260|molecule.ecocyc.CPD0-1260]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2347|molecule.ecocyc.CPD0-2347]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ETHAMLY-RXN`

## Notes

ETHANOL-AMINE -> AMMONIUM + ACETALD; direction=LEFT-TO-RIGHT
