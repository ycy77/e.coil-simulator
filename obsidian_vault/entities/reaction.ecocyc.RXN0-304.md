---
entity_id: "reaction.ecocyc.RXN0-304"
entity_type: "reaction"
name: "RXN0-304"
source_database: "EcoCyc"
source_id: "RXN0-304"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-304

`reaction.ecocyc.RXN0-304`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-304`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-ALLULOSE-6-PHOSPHATE -> FRUCTOSE-6P; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-ALLULOSE-6-PHOSPHATE -> FRUCTOSE-6P; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alsE (protein.P32719). Substrates: D-Allulose 6-phosphate (molecule.C18096). Products: β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P).

## Enriched Pathways

- `ecocyc.PWY0-44` D-allose degradation (EcoCyc)

## Annotation

D-ALLULOSE-6-PHOSPHATE -> FRUCTOSE-6P; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-44` D-allose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P32719|protein.P32719]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C18096|molecule.C18096]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-304`

## Notes

D-ALLULOSE-6-PHOSPHATE -> FRUCTOSE-6P; direction=LEFT-TO-RIGHT
