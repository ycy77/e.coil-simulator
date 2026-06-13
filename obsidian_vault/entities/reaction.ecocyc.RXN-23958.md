---
entity_id: "reaction.ecocyc.RXN-23958"
entity_type: "reaction"
name: "RXN-23958"
source_database: "EcoCyc"
source_id: "RXN-23958"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23958

`reaction.ecocyc.RXN-23958`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23958`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Tyr-tRNAPhe + WATER -> PHE-tRNAs + TYR + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Tyr-tRNAPhe + WATER -> PHE-tRNAs + TYR + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phenylalanine—tRNA ligase (complex.ecocyc.PHES-CPLX). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), L-Tyrosine (molecule.C00082).

## Annotation

Tyr-tRNAPhe + WATER -> PHE-tRNAs + TYR + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.PHES-CPLX|complex.ecocyc.PHES-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23958`

## Notes

Tyr-tRNAPhe + WATER -> PHE-tRNAs + TYR + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
