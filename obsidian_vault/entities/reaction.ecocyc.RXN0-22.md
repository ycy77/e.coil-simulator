---
entity_id: "reaction.ecocyc.RXN0-22"
entity_type: "reaction"
name: "guanosine:proton antiport"
source_database: "EcoCyc"
source_id: "RXN0-22"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# guanosine:proton antiport

`reaction.ecocyc.RXN0-22`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-22`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GUANOSINE + PROTON -> GUANOSINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: GUANOSINE + PROTON -> GUANOSINE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by nepI (protein.P0ADL1). Substrates: H+ (molecule.C00080), Guanosine (molecule.C00387). Products: H+ (molecule.C00080), Guanosine (molecule.C00387).

## Annotation

GUANOSINE + PROTON -> GUANOSINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ADL1|protein.P0ADL1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-22`

## Notes

GUANOSINE + PROTON -> GUANOSINE + PROTON; direction=REVERSIBLE
