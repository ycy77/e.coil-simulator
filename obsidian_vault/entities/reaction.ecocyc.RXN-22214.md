---
entity_id: "reaction.ecocyc.RXN-22214"
entity_type: "reaction"
name: "RXN-22214"
source_database: "EcoCyc"
source_id: "RXN-22214"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22214

`reaction.ecocyc.RXN-22214`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22214`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHOSPHO-ENOL-PYRUVATE + CPD-24197 -> CPD-24196 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHO-ENOL-PYRUVATE + CPD-24197 -> CPD-24196 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wcaK (protein.P71242). Substrates: Phosphoenolpyruvate (molecule.C00074), α-D-Gal-(1→4)-β-D-GlcA-(1→3)-2-O-Ac-α-D-Gal-(1→3)-α-L-Fuc-(1→4)-3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD-24197). Products: 4,6-pyr-α-D-Gal-(1→4)-β-D-GlcA-(1→3)-2-O-Ac-α-D-Gal-(1→3)-α-L-Fuc-(1→4)-3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD-24196), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Annotation

PHOSPHO-ENOL-PYRUVATE + CPD-24197 -> CPD-24196 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P71242|protein.P71242]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-24196|molecule.ecocyc.CPD-24196]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24197|molecule.ecocyc.CPD-24197]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22214`

## Notes

PHOSPHO-ENOL-PYRUVATE + CPD-24197 -> CPD-24196 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
