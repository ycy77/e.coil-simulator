---
entity_id: "reaction.ecocyc.RXN1ZN3-10"
entity_type: "reaction"
name: "RXN1ZN3-10"
source_database: "EcoCyc"
source_id: "RXN1ZN3-10"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN1ZN3-10

`reaction.ecocyc.RXN1ZN3-10`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN1ZN3-10`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD1ZN3-1 + ATP -> DETHIOBIOTIN + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD1ZN3-1 + ATP -> DETHIOBIOTIN + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), (7R,8S)-8-amino-7-(carboxyamino)nonanoate (molecule.ecocyc.CPD1ZN3-1). Products: ADP (molecule.C00008), H+ (molecule.C00080), Dethiobiotin (molecule.C01909), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD1ZN3-1 + ATP -> DETHIOBIOTIN + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01909|molecule.C01909]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD1ZN3-1|molecule.ecocyc.CPD1ZN3-1]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN1ZN3-10`

## Notes

CPD1ZN3-1 + ATP -> DETHIOBIOTIN + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
