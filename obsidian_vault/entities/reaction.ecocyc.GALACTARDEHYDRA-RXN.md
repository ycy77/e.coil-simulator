---
entity_id: "reaction.ecocyc.GALACTARDEHYDRA-RXN"
entity_type: "reaction"
name: "GALACTARDEHYDRA-RXN"
source_database: "EcoCyc"
source_id: "GALACTARDEHYDRA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GALACTARDEHYDRA-RXN

`reaction.ecocyc.GALACTARDEHYDRA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GALACTARDEHYDRA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the catabolism of galactarate. EcoCyc reaction equation: D-GALACTARATE -> 5-KETO-4-DEOXY-D-GLUCARATE + WATER; direction=LEFT-TO-RIGHT. This is the first reaction in the catabolism of galactarate.

## Biological Role

Catalyzed by galactarate dehydratase (complex.ecocyc.CPLX0-8537). Substrates: D-Galactarate (molecule.C00879). Products: H2O (molecule.C00001), 5-Dehydro-4-deoxy-D-glucarate (molecule.C00679).

## Enriched Pathways

- `ecocyc.GALACTARDEG-PWY` D-galactarate degradation I (EcoCyc)

## Annotation

This is the first reaction in the catabolism of galactarate.

## Pathways

- `ecocyc.GALACTARDEG-PWY` D-galactarate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8537|complex.ecocyc.CPLX0-8537]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00679|molecule.C00679]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00879|molecule.C00879]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7082|molecule.ecocyc.CPD-7082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GALACTARDEHYDRA-RXN`

## Notes

D-GALACTARATE -> 5-KETO-4-DEOXY-D-GLUCARATE + WATER; direction=LEFT-TO-RIGHT
