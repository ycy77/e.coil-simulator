---
entity_id: "reaction.ecocyc.RXN-2881"
entity_type: "reaction"
name: "RXN-2881"
source_database: "EcoCyc"
source_id: "RXN-2881"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-2881

`reaction.ecocyc.RXN-2881`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-2881`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FORMALDEHYDE + THF-GLU-N -> METHYLENE-THF-GLU-N + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FORMALDEHYDE + THF-GLU-N -> METHYLENE-THF-GLU-N + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Formaldehyde (molecule.C00067), THF-polyglutamate (molecule.C03541). Products: H2O (molecule.C00001), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N).

## Annotation

FORMALDEHYDE + THF-GLU-N -> METHYLENE-THF-GLU-N + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-2881`

## Notes

FORMALDEHYDE + THF-GLU-N -> METHYLENE-THF-GLU-N + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
