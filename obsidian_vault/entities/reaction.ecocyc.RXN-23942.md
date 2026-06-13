---
entity_id: "reaction.ecocyc.RXN-23942"
entity_type: "reaction"
name: "RXN-23942"
source_database: "EcoCyc"
source_id: "RXN-23942"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23942

`reaction.ecocyc.RXN-23942`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23942`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PRO-tRNAs + CYS + ATP -> Cys-tRNA-Pro + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PRO-tRNAs + CYS + ATP -> Cys-tRNA-Pro + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by proline—tRNA ligase (complex.ecocyc.PROS-CPLX). Substrates: ATP (molecule.C00002), L-Cysteine (molecule.C00097). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

PRO-tRNAs + CYS + ATP -> Cys-tRNA-Pro + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.PROS-CPLX|complex.ecocyc.PROS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23942`

## Notes

PRO-tRNAs + CYS + ATP -> Cys-tRNA-Pro + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
