---
entity_id: "reaction.ecocyc.RXN-12093"
entity_type: "reaction"
name: "RXN-12093"
source_database: "EcoCyc"
source_id: "RXN-12093"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12093

`reaction.ecocyc.RXN-12093`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12093`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13043 + AMMONIUM + ATP -> PROTON + 7-CYANO-7-DEAZAGUANINE + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-13043 + AMMONIUM + ATP -> PROTON + 7-CYANO-7-DEAZAGUANINE + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by queC (protein.P77756). Substrates: ATP (molecule.C00002), 7-Carboxy-7-carbaguanine (molecule.C20248), ammonium (molecule.ecocyc.AMMONIUM). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), 7-Cyano-7-carbaguanine (molecule.C15996).

## Enriched Pathways

- `ecocyc.PWY-6703` preQ0 biosynthesis (EcoCyc)

## Annotation

CPD-13043 + AMMONIUM + ATP -> PROTON + 7-CYANO-7-DEAZAGUANINE + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6703` preQ0 biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P77756|protein.P77756]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15996|molecule.C15996]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20248|molecule.C20248]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12093`

## Notes

CPD-13043 + AMMONIUM + ATP -> PROTON + 7-CYANO-7-DEAZAGUANINE + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
