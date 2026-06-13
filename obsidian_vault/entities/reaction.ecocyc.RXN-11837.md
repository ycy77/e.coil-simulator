---
entity_id: "reaction.ecocyc.RXN-11837"
entity_type: "reaction"
name: "RXN-11837"
source_database: "EcoCyc"
source_id: "RXN-11837"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11837

`reaction.ecocyc.RXN-11837`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11837`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

23S-rRNA-uridine1911-1915-1917 -> 23S-rRNA-pseudouridine1911-1915-1917; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 23S-rRNA-uridine1911-1915-1917 -> 23S-rRNA-pseudouridine1911-1915-1917; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rluD (protein.P33643). Substrates: a 23S rRNA uridine1911/1915/1917 (molecule.ecocyc.23S-rRNA-uridine1911-1915-1917). Products: a pseudouridine1911/1915/1917 in 23S rRNA (molecule.ecocyc.23S-rRNA-pseudouridine1911-1915-1917).

## Annotation

23S-rRNA-uridine1911-1915-1917 -> 23S-rRNA-pseudouridine1911-1915-1917; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P33643|protein.P33643]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-pseudouridine1911-1915-1917|molecule.ecocyc.23S-rRNA-pseudouridine1911-1915-1917]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-uridine1911-1915-1917|molecule.ecocyc.23S-rRNA-uridine1911-1915-1917]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11837`

## Notes

23S-rRNA-uridine1911-1915-1917 -> 23S-rRNA-pseudouridine1911-1915-1917; direction=PHYSIOL-LEFT-TO-RIGHT
