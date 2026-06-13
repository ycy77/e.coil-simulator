---
entity_id: "reaction.ecocyc.RXN-15147"
entity_type: "reaction"
name: "RXN-15147"
source_database: "EcoCyc"
source_id: "RXN-15147"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15147

`reaction.ecocyc.RXN-15147`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15147`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

O-SUCCINYL-L-HOMOSERINE -> SUC + CPD-15056 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: O-SUCCINYL-L-HOMOSERINE -> SUC + CPD-15056 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: O-Succinyl-L-homoserine (molecule.C01118). Products: Succinate (molecule.C00042), H+ (molecule.C00080), (Z)-2-aminobutenoate (molecule.ecocyc.CPD-15056).

## Annotation

O-SUCCINYL-L-HOMOSERINE -> SUC + CPD-15056 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15056|molecule.ecocyc.CPD-15056]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01118|molecule.C01118]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15147`

## Notes

O-SUCCINYL-L-HOMOSERINE -> SUC + CPD-15056 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
