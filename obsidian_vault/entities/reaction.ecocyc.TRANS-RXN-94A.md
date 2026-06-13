---
entity_id: "reaction.ecocyc.TRANS-RXN-94A"
entity_type: "reaction"
name: "melibiose:Na+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-94A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# melibiose:Na+ symport

`reaction.ecocyc.TRANS-RXN-94A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-94A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + MELIBIOSE -> NA+ + MELIBIOSE; direction=REVERSIBLE EcoCyc reaction equation: NA+ + MELIBIOSE -> NA+ + MELIBIOSE; direction=REVERSIBLE.

## Biological Role

Catalyzed by melB (protein.P02921). Substrates: Sodium cation (molecule.C01330), Melibiose (molecule.C05402). Products: Sodium cation (molecule.C01330), Melibiose (molecule.C05402).

## Annotation

NA+ + MELIBIOSE -> NA+ + MELIBIOSE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P02921|protein.P02921]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-94A`

## Notes

NA+ + MELIBIOSE -> NA+ + MELIBIOSE; direction=REVERSIBLE
