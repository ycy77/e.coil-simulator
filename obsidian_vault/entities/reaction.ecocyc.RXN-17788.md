---
entity_id: "reaction.ecocyc.RXN-17788"
entity_type: "reaction"
name: "RXN-17788"
source_database: "EcoCyc"
source_id: "RXN-17788"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17788

`reaction.ecocyc.RXN-17788`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17788`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10269 + ETF-Oxidized + PROTON -> CPD-19162 + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: CPD-10269 + ETF-Oxidized + PROTON -> CPD-19162 + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadE (protein.Q47146). Substrates: H+ (molecule.C00080), Palmitoleoyl-CoA (molecule.C21072). Products: (2E,9Z)-hexadec-2,9-enoyl-CoA (molecule.ecocyc.CPD-19162).

## Annotation

CPD-10269 + ETF-Oxidized + PROTON -> CPD-19162 + ETF-Reduced; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q47146|protein.Q47146]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-19162|molecule.ecocyc.CPD-19162]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C21072|molecule.C21072]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17788`

## Notes

CPD-10269 + ETF-Oxidized + PROTON -> CPD-19162 + ETF-Reduced; direction=REVERSIBLE
