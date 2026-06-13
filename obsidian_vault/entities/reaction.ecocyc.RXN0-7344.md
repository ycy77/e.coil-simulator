---
entity_id: "reaction.ecocyc.RXN0-7344"
entity_type: "reaction"
name: "RXN0-7344"
source_database: "EcoCyc"
source_id: "RXN0-7344"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7344

`reaction.ecocyc.RXN0-7344`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7344`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2664 + CPD-14553 -> CPD0-2665 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2664 + CPD-14553 -> CPD0-2665 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wcaC (protein.P71237). Substrates: UDP-alpha-D-galactose (molecule.C00052), α-L-Fuc-(1→4)-2/3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD0-2664). Products: UDP (molecule.C00015), H+ (molecule.C00080), α-D-Gal-(1→3)-α-L-Fuc-(1→4)-2/3-O-Ac-α-L-Fuc-(1->3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD0-2665).

## Enriched Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Annotation

CPD0-2664 + CPD-14553 -> CPD0-2665 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P71237|protein.P71237]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2665|molecule.ecocyc.CPD0-2665]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00052|molecule.C00052]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2664|molecule.ecocyc.CPD0-2664]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7344`

## Notes

CPD0-2664 + CPD-14553 -> CPD0-2665 + UDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
