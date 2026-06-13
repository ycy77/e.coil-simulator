---
entity_id: "reaction.ecocyc.LTARTDEHYDRA-RXN"
entity_type: "reaction"
name: "LTARTDEHYDRA-RXN"
source_database: "EcoCyc"
source_id: "LTARTDEHYDRA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LTARTDEHYDRA-RXN

`reaction.ecocyc.LTARTDEHYDRA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LTARTDEHYDRA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction of tartrate metabolism. EcoCyc reaction equation: TARTRATE -> OXALACETIC_ACID + WATER; direction=PHYSIOL-LEFT-TO-RIGHT. This is a reaction of tartrate metabolism.

## Biological Role

Catalyzed by L(+)-tartrate dehydratase (complex.ecocyc.LTARTDEHYDRA-CPLX). Substrates: (R,R)-Tartaric acid (molecule.C00898). Products: H2O (molecule.C00001), Oxaloacetate (molecule.C00036).

## Annotation

This is a reaction of tartrate metabolism.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.LTARTDEHYDRA-CPLX|complex.ecocyc.LTARTDEHYDRA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00898|molecule.C00898]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00552|molecule.C00552]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LTARTDEHYDRA-RXN`

## Notes

TARTRATE -> OXALACETIC_ACID + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
