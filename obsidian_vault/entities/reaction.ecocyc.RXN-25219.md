---
entity_id: "reaction.ecocyc.RXN-25219"
entity_type: "reaction"
name: "RXN-25219"
source_database: "EcoCyc"
source_id: "RXN-25219"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25219

`reaction.ecocyc.RXN-25219`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25219`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE + CPD-21359 -> CPD0-939 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE + CPD-21359 -> CPD0-939 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaL (protein.P27243). Substrates: α-D-GlcNAc-PP-Und (molecule.ecocyc.ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE), lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359). Products: H+ (molecule.C00080), di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), lipid A-core oligosaccharide (E. coli K-12 core type with D-GlcNAc) (molecule.ecocyc.CPD0-939).

## Annotation

ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE + CPD-21359 -> CPD0-939 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27243|protein.P27243]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-939|molecule.ecocyc.CPD0-939]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE|molecule.ecocyc.ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25219`

## Notes

ACETYL-D-GLUCOSAMINYLDIPHOSPHO-UNDECAPRE + CPD-21359 -> CPD0-939 + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
