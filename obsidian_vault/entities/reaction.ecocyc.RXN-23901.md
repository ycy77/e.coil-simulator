---
entity_id: "reaction.ecocyc.RXN-23901"
entity_type: "reaction"
name: "RXN-23901"
source_database: "EcoCyc"
source_id: "RXN-23901"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23901

`reaction.ecocyc.RXN-23901`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23901`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-915 + ASP-tRNAs -> Charged-ASP-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-915 + ASP-tRNAs -> Charged-ASP-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-aspartyl)adenylate (molecule.ecocyc.CPD0-915). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

CPD0-915 + ASP-tRNAs -> Charged-ASP-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-915|molecule.ecocyc.CPD0-915]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23901`

## Notes

CPD0-915 + ASP-tRNAs -> Charged-ASP-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
