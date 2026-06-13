---
entity_id: "reaction.ecocyc.RXN-25375"
entity_type: "reaction"
name: "lactate-CoA transferase"
source_database: "EcoCyc"
source_id: "RXN-25375"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lactate-CoA transferase

`reaction.ecocyc.RXN-25375`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25375`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETOACETYL-COA + L-LACTATE -> 3-KETOBUTYRATE + LACTOYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ACETOACETYL-COA + L-LACTATE -> 3-KETOBUTYRATE + LACTOYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ydiF (protein.P37766). Substrates: (S)-Lactate (molecule.C00186), Acetoacetyl-CoA (molecule.C00332). Products: Acetoacetate (molecule.C00164), (S)-lactoyl-CoA (molecule.ecocyc.LACTOYL-COA).

## Annotation

ACETOACETYL-COA + L-LACTATE -> 3-KETOBUTYRATE + LACTOYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37766|protein.P37766]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00164|molecule.C00164]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.LACTOYL-COA|molecule.ecocyc.LACTOYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00332|molecule.C00332]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25375`

## Notes

ACETOACETYL-COA + L-LACTATE -> 3-KETOBUTYRATE + LACTOYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT
