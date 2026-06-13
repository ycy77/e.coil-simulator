---
entity_id: "reaction.ecocyc.TRANS-RXN-342"
entity_type: "reaction"
name: "fosfomycin:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-342"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# fosfomycin:proton antiport

`reaction.ecocyc.TRANS-RXN-342`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-342`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-1113 + PROTON -> CPD0-1113 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1113 + PROTON -> CPD0-1113 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdtG (protein.P25744). Substrates: H+ (molecule.C00080), fosfomycin (molecule.ecocyc.CPD0-1113). Products: H+ (molecule.C00080), fosfomycin (molecule.ecocyc.CPD0-1113).

## Annotation

CPD0-1113 + PROTON -> CPD0-1113 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P25744|protein.P25744]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1113|molecule.ecocyc.CPD0-1113]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1113|molecule.ecocyc.CPD0-1113]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-342`

## Notes

CPD0-1113 + PROTON -> CPD0-1113 + PROTON; direction=REVERSIBLE
