---
entity_id: "reaction.ecocyc.GLUCARDEHYDRA-RXN"
entity_type: "reaction"
name: "GLUCARDEHYDRA-RXN"
source_database: "EcoCyc"
source_id: "GLUCARDEHYDRA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUCARDEHYDRA-RXN

`reaction.ecocyc.GLUCARDEHYDRA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCARDEHYDRA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in glucarate catabolism. EcoCyc reaction equation: D-GLUCARATE -> 5-KETO-4-DEOXY-D-GLUCARATE + WATER; direction=LEFT-TO-RIGHT. This is the first reaction in glucarate catabolism.

## Biological Role

Catalyzed by gudD (protein.P0AES2). Substrates: D-Glucarate (molecule.C00818). Products: H2O (molecule.C00001), 5-Dehydro-4-deoxy-D-glucarate (molecule.C00679).

## Enriched Pathways

- `ecocyc.GLUCARDEG-PWY` D-glucarate degradation I (EcoCyc)

## Annotation

This is the first reaction in glucarate catabolism.

## Pathways

- `ecocyc.GLUCARDEG-PWY` D-glucarate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[protein.P0AES2|protein.P0AES2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00679|molecule.C00679]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00818|molecule.C00818]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00879|molecule.C00879]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00898|molecule.C00898]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5401|molecule.ecocyc.CPD-5401]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1092|molecule.ecocyc.CPD0-1092]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1612|molecule.ecocyc.CPD0-1612]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1613|molecule.ecocyc.CPD0-1613]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUCARDEHYDRA-RXN`

## Notes

D-GLUCARATE -> 5-KETO-4-DEOXY-D-GLUCARATE + WATER; direction=LEFT-TO-RIGHT
