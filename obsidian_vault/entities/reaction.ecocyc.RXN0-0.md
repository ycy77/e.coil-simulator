---
entity_id: "reaction.ecocyc.RXN0-0"
entity_type: "reaction"
name: "RXN0-0"
source_database: "EcoCyc"
source_id: "RXN0-0"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-0

`reaction.ecocyc.RXN0-0`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-0`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

N-ACETYLNEURAMINATE -> N-ACETYLNEURAMINATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: N-ACETYLNEURAMINATE -> N-ACETYLNEURAMINATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nanC (protein.P69856). Substrates: N-Acetylneuraminate (molecule.C00270). Products: N-Acetylneuraminate (molecule.C00270).

## Annotation

N-ACETYLNEURAMINATE -> N-ACETYLNEURAMINATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P69856|protein.P69856]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00270|molecule.C00270]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00270|molecule.C00270]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-0`

## Notes

N-ACETYLNEURAMINATE -> N-ACETYLNEURAMINATE; direction=LEFT-TO-RIGHT
