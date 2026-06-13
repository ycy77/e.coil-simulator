---
entity_id: "reaction.ecocyc.RXN0-7484"
entity_type: "reaction"
name: "RXN0-7484"
source_database: "EcoCyc"
source_id: "RXN0-7484"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7484

`reaction.ecocyc.RXN0-7484`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7484`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2726 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + CPD-21542 + CARBON-DIOXIDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2726 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + CPD-21542 + CARBON-DIOXIDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkB (protein.P05050). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), 1,N6-α-hydroxypropanoadenine in DNA (molecule.ecocyc.CPD0-2726). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), malondialdehyde (molecule.ecocyc.CPD-21542), an adenine in DNA (molecule.ecocyc.DNA-Adenines).

## Annotation

CPD0-2726 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + CPD-21542 + CARBON-DIOXIDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P05050|protein.P05050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21542|molecule.ecocyc.CPD-21542]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DNA-Adenines|molecule.ecocyc.DNA-Adenines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2726|molecule.ecocyc.CPD0-2726]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7484`

## Notes

CPD0-2726 + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + CPD-21542 + CARBON-DIOXIDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT
