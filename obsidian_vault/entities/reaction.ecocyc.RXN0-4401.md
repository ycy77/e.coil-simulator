---
entity_id: "reaction.ecocyc.RXN0-4401"
entity_type: "reaction"
name: "RXN0-4401"
source_database: "EcoCyc"
source_id: "RXN0-4401"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4401

`reaction.ecocyc.RXN0-4401`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4401`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADH + WATER -> PROTON + NMNH + AMP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NADH + WATER -> PROTON + NMNH + AMP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by RNA decapping hydrolase (complex.ecocyc.CPLX0-7974). Substrates: H2O (molecule.C00001), NADH (molecule.C00004). Products: AMP (molecule.C00020), H+ (molecule.C00080), reduced β-nicotinamide D-ribonucleotide (molecule.ecocyc.NMNH).

## Annotation

NADH + WATER -> PROTON + NMNH + AMP; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7974|complex.ecocyc.CPLX0-7974]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NMNH|molecule.ecocyc.NMNH]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4401`

## Notes

NADH + WATER -> PROTON + NMNH + AMP; direction=LEFT-TO-RIGHT
