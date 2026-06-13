---
entity_id: "reaction.ecocyc.RXN-23928"
entity_type: "reaction"
name: "RXN-23928"
source_database: "EcoCyc"
source_id: "RXN-23928"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23928

`reaction.ecocyc.RXN-23928`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23928`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ASP-tRNAs + CPD-302 + ATP -> D-aspartyl-tRNA-Asp + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ASP-tRNAs + CPD-302 + ATP -> D-aspartyl-tRNA-Asp + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aspartate—tRNA ligase (complex.ecocyc.ASPS-CPLX). Substrates: ATP (molecule.C00002), D-Aspartate (molecule.C00402). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

ASP-tRNAs + CPD-302 + ATP -> D-aspartyl-tRNA-Asp + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ASPS-CPLX|complex.ecocyc.ASPS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00402|molecule.C00402]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23928`

## Notes

ASP-tRNAs + CPD-302 + ATP -> D-aspartyl-tRNA-Asp + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
