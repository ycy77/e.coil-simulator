---
entity_id: "reaction.ecocyc.RXN0-2044"
entity_type: "reaction"
name: "RXN0-2044"
source_database: "EcoCyc"
source_id: "RXN0-2044"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2044

`reaction.ecocyc.RXN0-2044`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2044`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-HYDROXYADIPYL-COA + NAD -> PROTON + 3-KETO-ADIPYL-COA + NADH; direction=REVERSIBLE EcoCyc reaction equation: 3-HYDROXYADIPYL-COA + NAD -> PROTON + 3-KETO-ADIPYL-COA + NADH; direction=REVERSIBLE.

## Biological Role

Catalyzed by paaH (protein.P76083). Substrates: NAD+ (molecule.C00003), (3S)-3-Hydroxyadipyl-CoA (molecule.C14145). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-Oxoadipyl-CoA (molecule.C02232).

## Enriched Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Annotation

3-HYDROXYADIPYL-COA + NAD -> PROTON + 3-KETO-ADIPYL-COA + NADH; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P76083|protein.P76083]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02232|molecule.C02232]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14145|molecule.C14145]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2044`

## Notes

3-HYDROXYADIPYL-COA + NAD -> PROTON + 3-KETO-ADIPYL-COA + NADH; direction=REVERSIBLE
