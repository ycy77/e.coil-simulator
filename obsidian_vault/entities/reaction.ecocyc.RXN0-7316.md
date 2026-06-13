---
entity_id: "reaction.ecocyc.RXN0-7316"
entity_type: "reaction"
name: "RXN0-7316"
source_database: "EcoCyc"
source_id: "RXN0-7316"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7316

`reaction.ecocyc.RXN0-7316`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7316`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUTARATE + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> CPD-381 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTARATE + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> CPD-381 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glutarate dioxygenase GlaH (complex.ecocyc.CPLX0-8201). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), Glutarate (molecule.C00489). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), (S)-2-Hydroxyglutarate (molecule.C03196).

## Enriched Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Annotation

GLUTARATE + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> CPD-381 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8201|complex.ecocyc.CPLX0-8201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03196|molecule.C03196]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00489|molecule.C00489]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7316`

## Notes

GLUTARATE + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> CPD-381 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
