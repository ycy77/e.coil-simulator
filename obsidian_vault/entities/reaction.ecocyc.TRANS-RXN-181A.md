---
entity_id: "reaction.ecocyc.TRANS-RXN-181A"
entity_type: "reaction"
name: "L-idonate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-181A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-idonate:proton symport

`reaction.ecocyc.TRANS-RXN-181A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-181A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + L-IDONATE -> L-IDONATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: PROTON + L-IDONATE -> L-IDONATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by idnT (protein.P39344). Substrates: H+ (molecule.C00080), L-idonate (molecule.ecocyc.L-IDONATE). Products: H+ (molecule.C00080), L-idonate (molecule.ecocyc.L-IDONATE).

## Annotation

PROTON + L-IDONATE -> L-IDONATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P39344|protein.P39344]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-IDONATE|molecule.ecocyc.L-IDONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-IDONATE|molecule.ecocyc.L-IDONATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-181A`

## Notes

PROTON + L-IDONATE -> L-IDONATE + PROTON; direction=REVERSIBLE
