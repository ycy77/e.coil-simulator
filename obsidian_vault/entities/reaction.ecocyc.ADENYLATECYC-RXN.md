---
entity_id: "reaction.ecocyc.ADENYLATECYC-RXN"
entity_type: "reaction"
name: "ADENYLATECYC-RXN"
source_database: "EcoCyc"
source_id: "ADENYLATECYC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADENYLATECYC-RXN

`reaction.ecocyc.ADENYLATECYC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENYLATECYC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes cyclic AMP. EcoCyc reaction equation: ATP -> CAMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes cyclic AMP.

## Biological Role

Catalyzed by cyaA (protein.P00936). Substrates: ATP (molecule.C00002). Products: Diphosphate (molecule.C00013), 3',5'-Cyclic AMP (molecule.C00575).

## Annotation

This reaction synthesizes cyclic AMP.

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P00936|protein.P00936]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00575|molecule.C00575]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1194|molecule.ecocyc.CPD0-1194]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ADENYLATECYC-RXN`

## Notes

ATP -> CAMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
