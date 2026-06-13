---
entity_id: "reaction.ecocyc.RXN-23936"
entity_type: "reaction"
name: "RXN-23936"
source_database: "EcoCyc"
source_id: "RXN-23936"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23936

`reaction.ecocyc.RXN-23936`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23936`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TYR-tRNAs + D-TYROSINE + ATP -> D-tyrosyl-tRNA-Tyr + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TYR-tRNAs + D-TYROSINE + ATP -> D-tyrosyl-tRNA-Tyr + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tyrosine—tRNA ligase (complex.ecocyc.TYRS-CPLX). Substrates: ATP (molecule.C00002), D-tyrosine (molecule.ecocyc.D-TYROSINE). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

TYR-tRNAs + D-TYROSINE + ATP -> D-tyrosyl-tRNA-Tyr + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.TYRS-CPLX|complex.ecocyc.TYRS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-TYROSINE|molecule.ecocyc.D-TYROSINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23936`

## Notes

TYR-tRNAs + D-TYROSINE + ATP -> D-tyrosyl-tRNA-Tyr + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
