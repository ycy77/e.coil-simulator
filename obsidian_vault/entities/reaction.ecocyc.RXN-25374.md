---
entity_id: "reaction.ecocyc.RXN-25374"
entity_type: "reaction"
name: "RXN-25374"
source_database: "EcoCyc"
source_id: "RXN-25374"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25374

`reaction.ecocyc.RXN-25374`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25374`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-27987 -> AMP + 7-CYANO-7-DEAZAGUANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-27987 -> AMP + 7-CYANO-7-DEAZAGUANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 7-iminomethyladenylyl-7-carbaguanine (molecule.ecocyc.CPD-27987). Products: AMP (molecule.C00020), H+ (molecule.C00080), 7-Cyano-7-carbaguanine (molecule.C15996).

## Annotation

CPD-27987 -> AMP + 7-CYANO-7-DEAZAGUANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15996|molecule.C15996]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-27987|molecule.ecocyc.CPD-27987]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25374`

## Notes

CPD-27987 -> AMP + 7-CYANO-7-DEAZAGUANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
