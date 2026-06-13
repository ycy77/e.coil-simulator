---
entity_id: "reaction.ecocyc.RXN-9623"
entity_type: "reaction"
name: "RXN-9623"
source_database: "EcoCyc"
source_id: "RXN-9623"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9623

`reaction.ecocyc.RXN-9623`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9623`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PALMITATE + CO-A + ATP -> PALMITYL-COA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PALMITATE + CO-A + ATP -> PALMITYL-COA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Hexadecanoic acid (molecule.C00249). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), Palmitoyl-CoA (molecule.C00154).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

PALMITATE + CO-A + ATP -> PALMITYL-COA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00154|molecule.C00154]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00249|molecule.C00249]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9623`

## Notes

PALMITATE + CO-A + ATP -> PALMITYL-COA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
