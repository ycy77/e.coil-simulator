---
entity_id: "reaction.ecocyc.RXN1ZN3-9"
entity_type: "reaction"
name: "RXN1ZN3-9"
source_database: "EcoCyc"
source_id: "RXN1ZN3-9"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN1ZN3-9

`reaction.ecocyc.RXN1ZN3-9`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN1ZN3-9`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIAMINONONANOATE + CARBON-DIOXIDE -> CPD1ZN3-1 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DIAMINONONANOATE + CARBON-DIOXIDE -> CPD1ZN3-1 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: CO2 (molecule.C00011), 7,8-Diaminononanoate (molecule.C01037). Products: H+ (molecule.C00080), (7R,8S)-8-amino-7-(carboxyamino)nonanoate (molecule.ecocyc.CPD1ZN3-1).

## Annotation

DIAMINONONANOATE + CARBON-DIOXIDE -> CPD1ZN3-1 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD1ZN3-1|molecule.ecocyc.CPD1ZN3-1]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01037|molecule.C01037]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN1ZN3-9`

## Notes

DIAMINONONANOATE + CARBON-DIOXIDE -> CPD1ZN3-1 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
