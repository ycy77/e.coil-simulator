---
entity_id: "reaction.ecocyc.RXN-23947"
entity_type: "reaction"
name: "RXN-23947"
source_database: "EcoCyc"
source_id: "RXN-23947"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23947

`reaction.ecocyc.RXN-23947`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23947`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THR-tRNAs + SER + ATP -> Seryl-tRNAThr + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: THR-tRNAs + SER + ATP -> Seryl-tRNAThr + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by threonine—tRNA ligase (complex.ecocyc.THRS-CPLX). Substrates: ATP (molecule.C00002), L-Serine (molecule.C00065). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

THR-tRNAs + SER + ATP -> Seryl-tRNAThr + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.THRS-CPLX|complex.ecocyc.THRS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23947`

## Notes

THR-tRNAs + SER + ATP -> Seryl-tRNAThr + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
