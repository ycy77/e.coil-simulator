---
entity_id: "reaction.ecocyc.RXN0-7077"
entity_type: "reaction"
name: "D-glucose:proton symport"
source_database: "EcoCyc"
source_id: "RXN0-7077"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-glucose:proton symport

`reaction.ecocyc.RXN0-7077`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7077`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

D-Glucose + PROTON -> D-Glucose + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-Glucose + PROTON -> D-Glucose + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by galP (protein.P0AEP1). Substrates: D-Glucose (molecule.C00031), H+ (molecule.C00080). Products: D-Glucose (molecule.C00031), H+ (molecule.C00080).

## Annotation

D-Glucose + PROTON -> D-Glucose + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEP1|protein.P0AEP1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7077`

## Notes

D-Glucose + PROTON -> D-Glucose + PROTON; direction=LEFT-TO-RIGHT
