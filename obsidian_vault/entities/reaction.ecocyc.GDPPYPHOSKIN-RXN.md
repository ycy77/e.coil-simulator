---
entity_id: "reaction.ecocyc.GDPPYPHOSKIN-RXN"
entity_type: "reaction"
name: "GDPPYPHOSKIN-RXN"
source_database: "EcoCyc"
source_id: "GDPPYPHOSKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GDPPYPHOSKIN-RXN

`reaction.ecocyc.GDPPYPHOSKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GDPPYPHOSKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is an alternative substrate reaction for E.C. reaction 2.7.6.5. In this instance GDP is used to produce ppGpp. EcoCyc reaction equation: ATP + GDP -> AMP + GUANOSINE-5DP-3DP + PROTON; direction=LEFT-TO-RIGHT. This is an alternative substrate reaction for E.C. reaction 2.7.6.5. In this instance GDP is used to produce ppGpp.

## Biological Role

Catalyzed by relA (protein.P0AG20), spoT (protein.P0AG24). Substrates: ATP (molecule.C00002), GDP (molecule.C00035). Products: AMP (molecule.C00020), H+ (molecule.C00080), Guanosine 3',5'-bis(diphosphate) (molecule.C01228).

## Enriched Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Annotation

This is an alternative substrate reaction for E.C. reaction 2.7.6.5. In this instance GDP is used to produce ppGpp.

## Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0AG20|protein.P0AG20]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AG24|protein.P0AG24]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GDPPYPHOSKIN-RXN`

## Notes

ATP + GDP -> AMP + GUANOSINE-5DP-3DP + PROTON; direction=LEFT-TO-RIGHT
