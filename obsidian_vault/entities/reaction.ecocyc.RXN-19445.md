---
entity_id: "reaction.ecocyc.RXN-19445"
entity_type: "reaction"
name: "RXN-19445"
source_database: "EcoCyc"
source_id: "RXN-19445"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19445

`reaction.ecocyc.RXN-19445`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19445`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-3-DIHYDROXYBENZOATE + Holo-EntB + ATP -> 23DHB-EntB + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-3-DIHYDROXYBENZOATE + Holo-EntB + ATP -> 23DHB-EntB + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2,3-dihydroxybenzoate-[aryl-carrier protein] ligase (complex.ecocyc.ENTE-CPLX). Substrates: ATP (molecule.C00002), 2,3-Dihydroxybenzoate (molecule.C00196). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

2-3-DIHYDROXYBENZOATE + Holo-EntB + ATP -> 23DHB-EntB + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.ENTE-CPLX|complex.ecocyc.ENTE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00196|molecule.C00196]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-2332|molecule.ecocyc.CPD0-2332]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-19445`

## Notes

2-3-DIHYDROXYBENZOATE + Holo-EntB + ATP -> 23DHB-EntB + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
