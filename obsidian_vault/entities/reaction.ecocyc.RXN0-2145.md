---
entity_id: "reaction.ecocyc.RXN0-2145"
entity_type: "reaction"
name: "RXN0-2145"
source_database: "EcoCyc"
source_id: "RXN0-2145"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2145

`reaction.ecocyc.RXN0-2145`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2145`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + Cis-Delta5-dodecenoyl-ACPs -> Trans-D3-cis-D5-dodecenoyl-ACPs + NADH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: NAD + Cis-Delta5-dodecenoyl-ACPs -> Trans-D3-cis-D5-dodecenoyl-ACPs + NADH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by enoyl-[acyl-carrier-protein] reductase (complex.ecocyc.CPLX0-8006). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY0-862` (5Z)-dodecenoate biosynthesis I (EcoCyc)

## Annotation

NAD + Cis-Delta5-dodecenoyl-ACPs -> Trans-D3-cis-D5-dodecenoyl-ACPs + NADH + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY0-862` (5Z)-dodecenoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8006|complex.ecocyc.CPLX0-8006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2145`

## Notes

NAD + Cis-Delta5-dodecenoyl-ACPs -> Trans-D3-cis-D5-dodecenoyl-ACPs + NADH + PROTON; direction=RIGHT-TO-LEFT
