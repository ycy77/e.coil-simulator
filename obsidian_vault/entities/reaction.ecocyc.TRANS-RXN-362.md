---
entity_id: "reaction.ecocyc.TRANS-RXN-362"
entity_type: "reaction"
name: "thymine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-362"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# thymine:proton symport

`reaction.ecocyc.TRANS-RXN-362`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-362`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

THYMINE + PROTON -> THYMINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: THYMINE + PROTON -> THYMINE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by rutG (protein.P75892). Substrates: H+ (molecule.C00080), Thymine (molecule.C00178). Products: H+ (molecule.C00080), Thymine (molecule.C00178).

## Annotation

THYMINE + PROTON -> THYMINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75892|protein.P75892]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-362`

## Notes

THYMINE + PROTON -> THYMINE + PROTON; direction=REVERSIBLE
