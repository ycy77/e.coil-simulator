---
entity_id: "reaction.ecocyc.TRANS-RXN-336"
entity_type: "reaction"
name: "electrogenic potassium:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-336"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# electrogenic potassium:proton antiport

`reaction.ecocyc.TRANS-RXN-336`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-336`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

K+ + PROTON -> K+ + PROTON; direction=REVERSIBLE EcoCyc reaction equation: K+ + PROTON -> K+ + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdtM (protein.P39386). Substrates: H+ (molecule.C00080), Potassium cation (molecule.C00238). Products: H+ (molecule.C00080), Potassium cation (molecule.C00238).

## Annotation

K+ + PROTON -> K+ + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39386|protein.P39386]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-336`

## Notes

K+ + PROTON -> K+ + PROTON; direction=REVERSIBLE
