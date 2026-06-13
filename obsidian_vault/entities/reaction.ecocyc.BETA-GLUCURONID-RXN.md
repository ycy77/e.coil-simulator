---
entity_id: "reaction.ecocyc.BETA-GLUCURONID-RXN"
entity_type: "reaction"
name: "BETA-GLUCURONID-RXN"
source_database: "EcoCyc"
source_id: "BETA-GLUCURONID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BETA-GLUCURONID-RXN

`reaction.ecocyc.BETA-GLUCURONID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BETA-GLUCURONID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the glucuronate pathway. EcoCyc reaction equation: WATER + Beta-D-Glucuronides -> D-Glucopyranuronate + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT. Part of the glucuronate pathway.

## Biological Role

Catalyzed by β-D-glucuronidase (complex.ecocyc.CPLX0-7662). Substrates: H2O (molecule.C00001), beta-D-Glucuronoside (molecule.C03033). Products: an alcohol (molecule.ecocyc.Alcohols), D-glucopyranuronate (molecule.ecocyc.D-Glucopyranuronate).

## Enriched Pathways

- `ecocyc.PWY-7247` β-D-glucuronide and D-glucuronate degradation (EcoCyc)

## Annotation

Part of the glucuronate pathway.

## Pathways

- `ecocyc.PWY-7247` β-D-glucuronide and D-glucuronate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7662|complex.ecocyc.CPLX0-7662]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Glucopyranuronate|molecule.ecocyc.D-Glucopyranuronate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03033|molecule.C03033]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BETA-GLUCURONID-RXN`

## Notes

WATER + Beta-D-Glucuronides -> D-Glucopyranuronate + Alcohols; direction=PHYSIOL-LEFT-TO-RIGHT
