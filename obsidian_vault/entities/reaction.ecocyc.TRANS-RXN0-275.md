---
entity_id: "reaction.ecocyc.TRANS-RXN0-275"
entity_type: "reaction"
name: "TRANS-RXN0-275"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-275"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-275

`reaction.ecocyc.TRANS-RXN0-275`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-275`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

CPD0-1193 -> CPD0-1193; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1193 -> CPD0-1193; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pgaA (protein.P69434). Substrates: a partially deacetylated poly-β-1,6-N-acetyl-D-glucosamine (molecule.ecocyc.CPD0-1193). Products: a partially deacetylated poly-β-1,6-N-acetyl-D-glucosamine (molecule.ecocyc.CPD0-1193).

## Enriched Pathways

- `ecocyc.PWY0-1609` poly-β-1,6-N-acetyl-D-glucosamine biosynthesis (EcoCyc)

## Annotation

CPD0-1193 -> CPD0-1193; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1609` poly-β-1,6-N-acetyl-D-glucosamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P69434|protein.P69434]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1193|molecule.ecocyc.CPD0-1193]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1193|molecule.ecocyc.CPD0-1193]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-275`

## Notes

CPD0-1193 -> CPD0-1193; direction=PHYSIOL-LEFT-TO-RIGHT
