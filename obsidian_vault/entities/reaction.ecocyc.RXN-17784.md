---
entity_id: "reaction.ecocyc.RXN-17784"
entity_type: "reaction"
name: "RXN-17784"
source_database: "EcoCyc"
source_id: "RXN-17784"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17784

`reaction.ecocyc.RXN-17784`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17784`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-18346 + ETF-Oxidized + PROTON -> CPD-19163 + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: CPD-18346 + ETF-Oxidized + PROTON -> CPD-19163 + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadE (protein.Q47146). Substrates: H+ (molecule.C00080), cis-Vaccenoyl-CoA (molecule.C21945). Products: (2E,11Z)-octadec-2,11-enoyl-CoA (molecule.ecocyc.CPD-19163).

## Annotation

CPD-18346 + ETF-Oxidized + PROTON -> CPD-19163 + ETF-Reduced; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q47146|protein.Q47146]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-19163|molecule.ecocyc.CPD-19163]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C21945|molecule.C21945]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17784`

## Notes

CPD-18346 + ETF-Oxidized + PROTON -> CPD-19163 + ETF-Reduced; direction=REVERSIBLE
