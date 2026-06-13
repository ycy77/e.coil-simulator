---
entity_id: "reaction.ecocyc.1.1.1.168-RXN"
entity_type: "reaction"
name: "1.1.1.168-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.168-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.1.1.168-RXN

`reaction.ecocyc.1.1.1.168-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.168-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PANTOYL-LACTONE + NADP -> 2-DEHYDROPANTOYL-LACTONE + NADPH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: PANTOYL-LACTONE + NADP -> 2-DEHYDROPANTOYL-LACTONE + NADPH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by DEHYDROPANTLACRED-MONOMER (protein.ecocyc.DEHYDROPANTLACRED-MONOMER). Substrates: NADP+ (molecule.C00006), (R)-pantolactone (molecule.ecocyc.PANTOYL-LACTONE). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2-dehydropantolactone (molecule.ecocyc.2-DEHYDROPANTOYL-LACTONE).

## Annotation

PANTOYL-LACTONE + NADP -> 2-DEHYDROPANTOYL-LACTONE + NADPH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.ecocyc.DEHYDROPANTLACRED-MONOMER|protein.ecocyc.DEHYDROPANTLACRED-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-DEHYDROPANTOYL-LACTONE|molecule.ecocyc.2-DEHYDROPANTOYL-LACTONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PANTOYL-LACTONE|molecule.ecocyc.PANTOYL-LACTONE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.1.1.168-RXN`

## Notes

PANTOYL-LACTONE + NADP -> 2-DEHYDROPANTOYL-LACTONE + NADPH + PROTON; direction=REVERSIBLE
