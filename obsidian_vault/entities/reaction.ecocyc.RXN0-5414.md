---
entity_id: "reaction.ecocyc.RXN0-5414"
entity_type: "reaction"
name: "RXN0-5414"
source_database: "EcoCyc"
source_id: "RXN0-5414"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5414

`reaction.ecocyc.RXN0-5414`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5414`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1192 + WATER -> CPD0-1193 + ACET; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1192 + WATER -> CPD0-1193 + ACET; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pgaB (protein.P75906). Substrates: H2O (molecule.C00001), poly-β-1,6-N-acetyl-D-glucosamine (molecule.ecocyc.CPD0-1192). Products: Acetate (molecule.C00033), a partially deacetylated poly-β-1,6-N-acetyl-D-glucosamine (molecule.ecocyc.CPD0-1193).

## Enriched Pathways

- `ecocyc.PWY0-1609` poly-β-1,6-N-acetyl-D-glucosamine biosynthesis (EcoCyc)

## Annotation

CPD0-1192 + WATER -> CPD0-1193 + ACET; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1609` poly-β-1,6-N-acetyl-D-glucosamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75906|protein.P75906]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1193|molecule.ecocyc.CPD0-1193]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1192|molecule.ecocyc.CPD0-1192]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5414`

## Notes

CPD0-1192 + WATER -> CPD0-1193 + ACET; direction=PHYSIOL-LEFT-TO-RIGHT
