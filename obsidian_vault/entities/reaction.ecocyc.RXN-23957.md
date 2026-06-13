---
entity_id: "reaction.ecocyc.RXN-23957"
entity_type: "reaction"
name: "RXN-23957"
source_database: "EcoCyc"
source_id: "RXN-23957"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23957

`reaction.ecocyc.RXN-23957`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23957`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHE-tRNAs + TYR + ATP -> Tyr-tRNAPhe + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHE-tRNAs + TYR + ATP -> Tyr-tRNAPhe + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phenylalanine—tRNA ligase (complex.ecocyc.PHES-CPLX). Substrates: ATP (molecule.C00002), L-Tyrosine (molecule.C00082). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

PHE-tRNAs + TYR + ATP -> Tyr-tRNAPhe + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.PHES-CPLX|complex.ecocyc.PHES-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23957`

## Notes

PHE-tRNAs + TYR + ATP -> Tyr-tRNAPhe + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
