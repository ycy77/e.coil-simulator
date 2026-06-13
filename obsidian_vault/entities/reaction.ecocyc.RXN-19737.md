---
entity_id: "reaction.ecocyc.RXN-19737"
entity_type: "reaction"
name: "RXN-19737"
source_database: "EcoCyc"
source_id: "RXN-19737"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19737

`reaction.ecocyc.RXN-19737`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19737`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-ACETYL-D-GLUCOSAMINE + CPD-21359 -> CPD0-939 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: UDP-N-ACETYL-D-GLUCOSAMINE + CPD-21359 -> CPD0-939 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043), lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359). Products: UDP (molecule.C00015), H+ (molecule.C00080), lipid A-core oligosaccharide (E. coli K-12 core type with D-GlcNAc) (molecule.ecocyc.CPD0-939).

## Annotation

UDP-N-ACETYL-D-GLUCOSAMINE + CPD-21359 -> CPD0-939 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-939|molecule.ecocyc.CPD0-939]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19737`

## Notes

UDP-N-ACETYL-D-GLUCOSAMINE + CPD-21359 -> CPD0-939 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
