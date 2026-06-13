---
entity_id: "reaction.ecocyc.RXN0-7389"
entity_type: "reaction"
name: "RXN0-7389"
source_database: "EcoCyc"
source_id: "RXN0-7389"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7389

`reaction.ecocyc.RXN0-7389`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7389`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2701 -> CPD0-1123; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2701 -> CPD0-1123; direction=REVERSIBLE.

## Biological Role

Catalyzed by nanQ (protein.P45424). Substrates: aceneuramate (molecule.ecocyc.CPD0-2701). Products: N-acetyl-β-neuraminate (molecule.ecocyc.CPD0-1123).

## Enriched Pathways

- `ecocyc.PWY0-1324` N-acetylneuraminate and N-acetylmannosamine degradation I (EcoCyc)

## Annotation

CPD0-2701 -> CPD0-1123; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1324` N-acetylneuraminate and N-acetylmannosamine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P45424|protein.P45424]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1123|molecule.ecocyc.CPD0-1123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2701|molecule.ecocyc.CPD0-2701]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7389`

## Notes

CPD0-2701 -> CPD0-1123; direction=REVERSIBLE
