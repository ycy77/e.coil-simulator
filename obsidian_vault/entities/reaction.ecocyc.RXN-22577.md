---
entity_id: "reaction.ecocyc.RXN-22577"
entity_type: "reaction"
name: "RXN-22577"
source_database: "EcoCyc"
source_id: "RXN-22577"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22577

`reaction.ecocyc.RXN-22577`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22577`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Represents the spontaneous hydrolytic deamination of cytosine in DNA . EcoCyc reaction equation: DNA-Cytosines + WATER -> DNA-with-Uracils + AMMONIA; direction=PHYSIOL-LEFT-TO-RIGHT. Represents the spontaneous hydrolytic deamination of cytosine in DNA .

## Biological Role

Substrates: H2O (molecule.C00001), a cytosine in DNA (molecule.ecocyc.DNA-Cytosines). Products: Ammonia (molecule.C00014).

## Annotation

Represents the spontaneous hydrolytic deamination of cytosine in DNA .

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-Cytosines|molecule.ecocyc.DNA-Cytosines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22577`

## Notes

DNA-Cytosines + WATER -> DNA-with-Uracils + AMMONIA; direction=PHYSIOL-LEFT-TO-RIGHT
