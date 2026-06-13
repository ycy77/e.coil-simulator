---
entity_id: "reaction.ecocyc.RXN-17779"
entity_type: "reaction"
name: "RXN-17779"
source_database: "EcoCyc"
source_id: "RXN-17779"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17779

`reaction.ecocyc.RXN-17779`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17779`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19144 + ETF-Oxidized + PROTON -> CPD-19170 + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: CPD-19144 + ETF-Oxidized + PROTON -> CPD-19170 + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadE (protein.Q47146). Substrates: H+ (molecule.C00080), (7Z)-hexadecenoyl-CoA (molecule.ecocyc.CPD-19144). Products: (2E,7Z)-hexadec-2,7-dienoyl-CoA (molecule.ecocyc.CPD-19170).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-19144 + ETF-Oxidized + PROTON -> CPD-19170 + ETF-Reduced; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q47146|protein.Q47146]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-19170|molecule.ecocyc.CPD-19170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19144|molecule.ecocyc.CPD-19144]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17779`

## Notes

CPD-19144 + ETF-Oxidized + PROTON -> CPD-19170 + ETF-Reduced; direction=REVERSIBLE
