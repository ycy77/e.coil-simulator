---
entity_id: "reaction.ecocyc.TRANS-RXN0-452"
entity_type: "reaction"
name: "p-aminobenzoyl glutamate: proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-452"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# p-aminobenzoyl glutamate: proton symport

`reaction.ecocyc.TRANS-RXN0-452`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-452`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-889 + PROTON -> CPD0-889 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-889 + PROTON -> CPD0-889 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by abgT (protein.P46133). Substrates: H+ (molecule.C00080), N-(4-aminobenzoyl)-L-glutamate (molecule.ecocyc.CPD0-889). Products: H+ (molecule.C00080), N-(4-aminobenzoyl)-L-glutamate (molecule.ecocyc.CPD0-889).

## Annotation

CPD0-889 + PROTON -> CPD0-889 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P46133|protein.P46133]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-889|molecule.ecocyc.CPD0-889]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-889|molecule.ecocyc.CPD0-889]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-2841|molecule.ecocyc.CPD-2841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-452`

## Notes

CPD0-889 + PROTON -> CPD0-889 + PROTON; direction=REVERSIBLE
