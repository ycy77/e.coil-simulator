---
entity_id: "reaction.ecocyc.RXN0-7341"
entity_type: "reaction"
name: "RXN0-7341"
source_database: "EcoCyc"
source_id: "RXN0-7341"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7341

`reaction.ecocyc.RXN0-7341`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7341`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12773 + CPD-13118 -> CPD0-2660 + GDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12773 + CPD-13118 -> CPD0-2660 + GDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wcaI (protein.P32057). Substrates: GDP-L-fucose (molecule.C00325), α-D-Glc-PP-Und (molecule.ecocyc.CPD-12773). Products: GDP (molecule.C00035), H+ (molecule.C00080), α-L-Fuc-(1->3)-α-D-Glc-PP-Und (molecule.ecocyc.CPD0-2660).

## Enriched Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Annotation

CPD-12773 + CPD-13118 -> CPD0-2660 + GDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P32057|protein.P32057]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2660|molecule.ecocyc.CPD0-2660]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00325|molecule.C00325]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12773|molecule.ecocyc.CPD-12773]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7341`

## Notes

CPD-12773 + CPD-13118 -> CPD0-2660 + GDP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
