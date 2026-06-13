---
entity_id: "reaction.ecocyc.RXN-22216"
entity_type: "reaction"
name: "RXN-22216"
source_database: "EcoCyc"
source_id: "RXN-22216"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22216

`reaction.ecocyc.RXN-22216`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22216`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-GLUCURONATE + CPD0-2666 -> CPD-24198 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: UDP-GLUCURONATE + CPD0-2666 -> CPD-24198 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wcaA (protein.P77414). Substrates: UDP-glucuronate (molecule.C00167), 2-O-Ac-α-D-Gal-(1→3)-α-L-Fuc-(1→4)-2/3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD0-2666). Products: UDP (molecule.C00015), H+ (molecule.C00080), β-D-GlcA-(1→3)-2-O-Ac-α-D-Gal-(1→3)-α-L-Fuc-(1→4)-3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD-24198).

## Enriched Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Annotation

UDP-GLUCURONATE + CPD0-2666 -> CPD-24198 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77414|protein.P77414]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24198|molecule.ecocyc.CPD-24198]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00167|molecule.C00167]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2666|molecule.ecocyc.CPD0-2666]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22216`

## Notes

UDP-GLUCURONATE + CPD0-2666 -> CPD-24198 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
