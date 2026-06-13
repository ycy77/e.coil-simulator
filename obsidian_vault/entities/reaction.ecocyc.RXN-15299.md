---
entity_id: "reaction.ecocyc.RXN-15299"
entity_type: "reaction"
name: "RXN-15299"
source_database: "EcoCyc"
source_id: "RXN-15299"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15299

`reaction.ecocyc.RXN-15299`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15299`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12693 + NAD -> CPD-18718 + NADH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: CPD-12693 + NAD -> CPD-18718 + NADH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 3-sulfolactaldehyde reductase (complex.ecocyc.CPLX0-7794). Substrates: NAD+ (molecule.C00003), (2S)-2,3-Dihydroxypropane-1-sulfonate (molecule.C22383). Products: NADH (molecule.C00004), H+ (molecule.C00080), (2S)-3-Sulfolactaldehyde (molecule.C21181).

## Enriched Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Annotation

CPD-12693 + NAD -> CPD-18718 + NADH + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7794|complex.ecocyc.CPLX0-7794]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21181|molecule.C21181]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C22383|molecule.C22383]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15299`

## Notes

CPD-12693 + NAD -> CPD-18718 + NADH + PROTON; direction=RIGHT-TO-LEFT
