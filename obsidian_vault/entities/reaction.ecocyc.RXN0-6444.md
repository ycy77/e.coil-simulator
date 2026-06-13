---
entity_id: "reaction.ecocyc.RXN0-6444"
entity_type: "reaction"
name: "RXN0-6444"
source_database: "EcoCyc"
source_id: "RXN0-6444"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6444

`reaction.ecocyc.RXN0-6444`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6444`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

URACIL + OXYGEN-MOLECULE + FMNH2 + NADH -> CPD0-2331 + FMN + WATER + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: URACIL + OXYGEN-MOLECULE + FMNH2 + NADH -> CPD0-2331 + FMN + WATER + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rutA (protein.P75898). Substrates: NADH (molecule.C00004), Oxygen (molecule.C00007), Uracil (molecule.C00106), Reduced FMN (molecule.C01847). Products: H2O (molecule.C00001), NAD+ (molecule.C00003), FMN (molecule.C00061), H+ (molecule.C00080), Ureidoacrylate (molecule.C20254).

## Enriched Pathways

- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Annotation

URACIL + OXYGEN-MOLECULE + FMNH2 + NADH -> CPD0-2331 + FMN + WATER + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P75898|protein.P75898]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20254|molecule.C20254]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6444`

## Notes

URACIL + OXYGEN-MOLECULE + FMNH2 + NADH -> CPD0-2331 + FMN + WATER + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
