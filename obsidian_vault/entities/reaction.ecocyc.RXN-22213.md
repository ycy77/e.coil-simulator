---
entity_id: "reaction.ecocyc.RXN-22213"
entity_type: "reaction"
name: "RXN-22213"
source_database: "EcoCyc"
source_id: "RXN-22213"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22213

`reaction.ecocyc.RXN-22213`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22213`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-24196 -> Colanic-Acid-PP-Und + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-24196 -> Colanic-Acid-PP-Und + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wcaD (protein.P71238). Substrates: 4,6-pyr-α-D-Gal-(1→4)-β-D-GlcA-(1→3)-2-O-Ac-α-D-Gal-(1→3)-α-L-Fuc-(1→4)-3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD-24196). Products: H+ (molecule.C00080), di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), colanic acid (E. coli K-12) attached to lipid anchor (molecule.ecocyc.Colanic-Acid-PP-Und).

## Enriched Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Annotation

CPD-24196 -> Colanic-Acid-PP-Und + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P71238|protein.P71238]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Colanic-Acid-PP-Und|molecule.ecocyc.Colanic-Acid-PP-Und]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24196|molecule.ecocyc.CPD-24196]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22213`

## Notes

CPD-24196 -> Colanic-Acid-PP-Und + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
