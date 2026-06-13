---
entity_id: "reaction.ecocyc.RXN0-7230"
entity_type: "reaction"
name: "RXN0-7230"
source_database: "EcoCyc"
source_id: "RXN0-7230"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7230

`reaction.ecocyc.RXN0-7230`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7230`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This is the first reaction in the betaine biosynthetic pathway. EcoCyc reaction equation: ETR-Quinones + CHOLINE -> ETR-Quinols + BETAINE_ALDEHYDE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first reaction in the betaine biosynthetic pathway.

## Biological Role

Catalyzed by betA (protein.P17444). Substrates: Choline (molecule.C00114). Products: Betaine aldehyde (molecule.C00576).

## Annotation

This is the first reaction in the betaine biosynthetic pathway.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P17444|protein.P17444]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00576|molecule.C00576]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7230`

## Notes

ETR-Quinones + CHOLINE -> ETR-Quinols + BETAINE_ALDEHYDE; direction=PHYSIOL-LEFT-TO-RIGHT
