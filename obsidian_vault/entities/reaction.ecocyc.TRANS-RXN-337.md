---
entity_id: "reaction.ecocyc.TRANS-RXN-337"
entity_type: "reaction"
name: "dequalinium:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-337"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# dequalinium:proton antiport

`reaction.ecocyc.TRANS-RXN-337`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-337`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-20894 + PROTON -> CPD-20894 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-20894 + PROTON -> CPD-20894 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdfA (protein.P0AEY8). Substrates: H+ (molecule.C00080), dequalinium (molecule.ecocyc.CPD-20894). Products: H+ (molecule.C00080), dequalinium (molecule.ecocyc.CPD-20894).

## Annotation

CPD-20894 + PROTON -> CPD-20894 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEY8|protein.P0AEY8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20894|molecule.ecocyc.CPD-20894]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20894|molecule.ecocyc.CPD-20894]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-20898|molecule.ecocyc.CPD-20898]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-337`

## Notes

CPD-20894 + PROTON -> CPD-20894 + PROTON; direction=REVERSIBLE
