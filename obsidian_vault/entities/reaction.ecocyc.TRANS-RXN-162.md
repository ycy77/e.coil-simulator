---
entity_id: "reaction.ecocyc.TRANS-RXN-162"
entity_type: "reaction"
name: "L-glutamate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-162"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-glutamate:proton symport

`reaction.ecocyc.TRANS-RXN-162`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-162`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + GLT -> PROTON + GLT; direction=REVERSIBLE EcoCyc reaction equation: PROTON + GLT -> PROTON + GLT; direction=REVERSIBLE.

## Biological Role

Catalyzed by gltP (protein.P21345). Substrates: L-Glutamate (molecule.C00025), H+ (molecule.C00080). Products: L-Glutamate (molecule.C00025), H+ (molecule.C00080).

## Annotation

PROTON + GLT -> PROTON + GLT; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21345|protein.P21345]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-162`

## Notes

PROTON + GLT -> PROTON + GLT; direction=REVERSIBLE
