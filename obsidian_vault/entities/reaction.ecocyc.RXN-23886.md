---
entity_id: "reaction.ecocyc.RXN-23886"
entity_type: "reaction"
name: "RXN-23886"
source_database: "EcoCyc"
source_id: "RXN-23886"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23886

`reaction.ecocyc.RXN-23886`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23886`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNAs + L-Amino-Acids + ATP -> Charged-tRNAs + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNAs + L-Amino-Acids + ATP -> Charged-tRNAs + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Amino acid (molecule.C00151). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

tRNAs + L-Amino-Acids + ATP -> Charged-tRNAs + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00151|molecule.C00151]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23886`

## Notes

tRNAs + L-Amino-Acids + ATP -> Charged-tRNAs + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
