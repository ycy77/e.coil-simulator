---
entity_id: "reaction.ecocyc.TRANS-RXN-122A"
entity_type: "reaction"
name: "aspartate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-122A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# aspartate:proton symport

`reaction.ecocyc.TRANS-RXN-122A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-122A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + L-ASPARTATE -> PROTON + L-ASPARTATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + L-ASPARTATE -> PROTON + L-ASPARTATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by dctA (protein.P0A830), dauA (protein.P0AFR2), gltP (protein.P21345). Substrates: L-Aspartate (molecule.C00049), H+ (molecule.C00080). Products: L-Aspartate (molecule.C00049), H+ (molecule.C00080).

## Annotation

PROTON + L-ASPARTATE -> PROTON + L-ASPARTATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFR2|protein.P0AFR2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P21345|protein.P21345]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-122A`

## Notes

PROTON + L-ASPARTATE -> PROTON + L-ASPARTATE; direction=REVERSIBLE
