---
entity_id: "reaction.ecocyc.RXN0-5294"
entity_type: "reaction"
name: "RXN0-5294"
source_database: "EcoCyc"
source_id: "RXN0-5294"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5294

`reaction.ecocyc.RXN0-5294`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5294`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-24196 + CPD-21359 -> CPD0-1101 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-24196 + CPD-21359 -> CPD0-1101 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaL (protein.P27243). Substrates: lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359), 4,6-pyr-α-D-Gal-(1→4)-β-D-GlcA-(1→3)-2-O-Ac-α-D-Gal-(1→3)-α-L-Fuc-(1→4)-3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD-24196). Products: H+ (molecule.C00080), di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), E. coli MLPS (molecule.ecocyc.CPD0-1101).

## Annotation

CPD-24196 + CPD-21359 -> CPD0-1101 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27243|protein.P27243]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1101|molecule.ecocyc.CPD0-1101]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24196|molecule.ecocyc.CPD-24196]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5294`

## Notes

CPD-24196 + CPD-21359 -> CPD0-1101 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
