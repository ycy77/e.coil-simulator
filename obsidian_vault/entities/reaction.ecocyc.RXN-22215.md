---
entity_id: "reaction.ecocyc.RXN-22215"
entity_type: "reaction"
name: "RXN-22215"
source_database: "EcoCyc"
source_id: "RXN-22215"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22215

`reaction.ecocyc.RXN-22215`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22215`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-14553 + CPD-24198 -> CPD-24197 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-14553 + CPD-24198 -> CPD-24197 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wcaL (protein.P71243). Substrates: UDP-alpha-D-galactose (molecule.C00052), β-D-GlcA-(1→3)-2-O-Ac-α-D-Gal-(1→3)-α-L-Fuc-(1→4)-3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD-24198). Products: UDP (molecule.C00015), H+ (molecule.C00080), α-D-Gal-(1→4)-β-D-GlcA-(1→3)-2-O-Ac-α-D-Gal-(1→3)-α-L-Fuc-(1→4)-3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD-24197).

## Enriched Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Annotation

CPD-14553 + CPD-24198 -> CPD-24197 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P71243|protein.P71243]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24197|molecule.ecocyc.CPD-24197]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00052|molecule.C00052]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24198|molecule.ecocyc.CPD-24198]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22215`

## Notes

CPD-14553 + CPD-24198 -> CPD-24197 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
