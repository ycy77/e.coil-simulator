---
entity_id: "reaction.ecocyc.RXN-12071"
entity_type: "reaction"
name: "RXN-12071"
source_database: "EcoCyc"
source_id: "RXN-12071"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12071

`reaction.ecocyc.RXN-12071`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12071`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13034 + NAD -> CPD-10796 + NADH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-13034 + NAD -> CPD-10796 + NADH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hcaB (protein.P0CI31). Substrates: NAD+ (molecule.C00003), (2E)-3-(5,6-dihydroxycyclohexa-1,3-dien-1-yl)prop-2-enoate (molecule.ecocyc.CPD-13034). Products: NADH (molecule.C00004), H+ (molecule.C00080), trans-2,3-Dihydroxycinnamate (molecule.C12623).

## Enriched Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

CPD-13034 + NAD -> CPD-10796 + NADH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0CI31|protein.P0CI31]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C12623|molecule.C12623]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13034|molecule.ecocyc.CPD-13034]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12071`

## Notes

CPD-13034 + NAD -> CPD-10796 + NADH + PROTON; direction=LEFT-TO-RIGHT
