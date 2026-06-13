---
entity_id: "reaction.ecocyc.RXN-19474"
entity_type: "reaction"
name: "RXN-19474"
source_database: "EcoCyc"
source_id: "RXN-19474"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19474

`reaction.ecocyc.RXN-19474`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19474`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SER + Holo-EntF + ATP -> Seryl-EntF + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SER + Holo-EntF + ATP -> Seryl-EntF + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by entF (protein.P11454). Substrates: ATP (molecule.C00002), L-Serine (molecule.C00065). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

SER + Holo-EntF + ATP -> Seryl-EntF + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P11454|protein.P11454]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-19474`

## Notes

SER + Holo-EntF + ATP -> Seryl-EntF + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
