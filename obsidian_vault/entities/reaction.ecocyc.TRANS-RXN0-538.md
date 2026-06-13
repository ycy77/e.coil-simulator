---
entity_id: "reaction.ecocyc.TRANS-RXN0-538"
entity_type: "reaction"
name: "pseudouridine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-538"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# pseudouridine:proton symport

`reaction.ecocyc.TRANS-RXN0-538`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-538`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-497 + PROTON -> CPD-497 + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-497 + PROTON -> CPD-497 + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by psuT (protein.P33024). Substrates: H+ (molecule.C00080), Pseudouridine (molecule.C02067). Products: H+ (molecule.C00080), Pseudouridine (molecule.C02067).

## Annotation

CPD-497 + PROTON -> CPD-497 + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33024|protein.P33024]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02067|molecule.C02067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02067|molecule.C02067]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-538`

## Notes

CPD-497 + PROTON -> CPD-497 + PROTON; direction=LEFT-TO-RIGHT
