---
entity_id: "reaction.ecocyc.RXN0-268"
entity_type: "reaction"
name: "RXN0-268"
source_database: "EcoCyc"
source_id: "RXN0-268"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-268

`reaction.ecocyc.RXN0-268`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-268`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROPIONYL-COA + SUC -> PROPIONATE + SUC-COA; direction=REVERSIBLE EcoCyc reaction equation: PROPIONYL-COA + SUC -> PROPIONATE + SUC-COA; direction=REVERSIBLE.

## Biological Role

Catalyzed by scpC (protein.P52043). Substrates: Succinate (molecule.C00042), Propanoyl-CoA (molecule.C00100). Products: Succinyl-CoA (molecule.C00091), Propanoate (molecule.C00163).

## Enriched Pathways

- `ecocyc.PWY0-43` conversion of succinate to propanoate (EcoCyc)

## Annotation

PROPIONYL-COA + SUC -> PROPIONATE + SUC-COA; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-43` conversion of succinate to propanoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P52043|protein.P52043]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00163|molecule.C00163]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-268`

## Notes

PROPIONYL-COA + SUC -> PROPIONATE + SUC-COA; direction=REVERSIBLE
