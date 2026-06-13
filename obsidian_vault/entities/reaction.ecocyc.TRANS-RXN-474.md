---
entity_id: "reaction.ecocyc.TRANS-RXN-474"
entity_type: "reaction"
name: "guanosine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-474"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# guanosine:proton symport

`reaction.ecocyc.TRANS-RXN-474`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-474`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GUANOSINE + PROTON -> GUANOSINE + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GUANOSINE + PROTON -> GUANOSINE + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nupG (protein.P0AFF4). Substrates: H+ (molecule.C00080), Guanosine (molecule.C00387). Products: H+ (molecule.C00080), Guanosine (molecule.C00387).

## Annotation

GUANOSINE + PROTON -> GUANOSINE + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-474`

## Notes

GUANOSINE + PROTON -> GUANOSINE + PROTON; direction=LEFT-TO-RIGHT
