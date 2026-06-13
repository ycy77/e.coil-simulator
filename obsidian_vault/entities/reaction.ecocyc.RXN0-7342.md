---
entity_id: "reaction.ecocyc.RXN0-7342"
entity_type: "reaction"
name: "RXN0-7342"
source_database: "EcoCyc"
source_id: "RXN0-7342"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7342

`reaction.ecocyc.RXN0-7342`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7342`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2660 + ACETYL-COA -> CPD0-2661 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2660 + ACETYL-COA -> CPD0-2661 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wcaF (protein.P0ACD2). Substrates: Acetyl-CoA (molecule.C00024), α-L-Fuc-(1->3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD0-2660). Products: CoA (molecule.C00010), 2/3-O-Ac-α-L-Fuc-(1→3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD0-2661).

## Enriched Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Annotation

CPD0-2660 + ACETYL-COA -> CPD0-2661 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ACD2|protein.P0ACD2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2661|molecule.ecocyc.CPD0-2661]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2660|molecule.ecocyc.CPD0-2660]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7342`

## Notes

CPD0-2660 + ACETYL-COA -> CPD0-2661 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
