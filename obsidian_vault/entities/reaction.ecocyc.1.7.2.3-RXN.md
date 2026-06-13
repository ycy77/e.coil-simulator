---
entity_id: "reaction.ecocyc.1.7.2.3-RXN"
entity_type: "reaction"
name: "1.7.2.3-RXN"
source_database: "EcoCyc"
source_id: "1.7.2.3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.7.2.3-RXN

`reaction.ecocyc.1.7.2.3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.7.2.3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

TRIMETHYLAMINE + Cytochromes-C-Oxidized + WATER -> TRIMETHYLAMINE-N-O + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: TRIMETHYLAMINE + Cytochromes-C-Oxidized + WATER -> TRIMETHYLAMINE-N-O + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: H2O (molecule.C00001), Trimethylamine (molecule.C00565). Products: H+ (molecule.C00080), Trimethylamine N-oxide (molecule.C01104).

## Annotation

TRIMETHYLAMINE + Cytochromes-C-Oxidized + WATER -> TRIMETHYLAMINE-N-O + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01104|molecule.C01104]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00565|molecule.C00565]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.7.2.3-RXN`

## Notes

TRIMETHYLAMINE + Cytochromes-C-Oxidized + WATER -> TRIMETHYLAMINE-N-O + Cytochromes-C-Reduced + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
