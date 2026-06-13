---
entity_id: "reaction.ecocyc.RXN-9644"
entity_type: "reaction"
name: "RXN-9644"
source_database: "EcoCyc"
source_id: "RXN-9644"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9644

`reaction.ecocyc.RXN-9644`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9644`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OLEATE-CPD + CO-A + ATP -> OLEOYL-COA + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: OLEATE-CPD + CO-A + ATP -> OLEOYL-COA + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), CoA (molecule.C00010), (9Z)-Octadecenoic acid (molecule.C00712). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), Oleoyl-CoA (molecule.C00510).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

OLEATE-CPD + CO-A + ATP -> OLEOYL-COA + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00510|molecule.C00510]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00712|molecule.C00712]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9644`

## Notes

OLEATE-CPD + CO-A + ATP -> OLEOYL-COA + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
