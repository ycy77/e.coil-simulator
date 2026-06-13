---
entity_id: "reaction.ecocyc.RXN-19242"
entity_type: "reaction"
name: "RXN-19242"
source_database: "EcoCyc"
source_id: "RXN-19242"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19242

`reaction.ecocyc.RXN-19242`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19242`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-20741 + Light -> CPD-20735; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-20741 + Light -> CPD-20735; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phrB (protein.P00914). Substrates: hν (molecule.ecocyc.Light). Products: two adjacent 2'-deoxycytidines in DNA (molecule.ecocyc.CPD-20735).

## Annotation

CPD-20741 + Light -> CPD-20735; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P00914|protein.P00914]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-20735|molecule.ecocyc.CPD-20735]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19242`

## Notes

CPD-20741 + Light -> CPD-20735; direction=PHYSIOL-LEFT-TO-RIGHT
