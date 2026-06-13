---
entity_id: "reaction.ecocyc.RXN-17792"
entity_type: "reaction"
name: "RXN-17792"
source_database: "EcoCyc"
source_id: "RXN-17792"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17792

`reaction.ecocyc.RXN-17792`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17792`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19147 + ETF-Oxidized + PROTON -> CPD-19161 + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: CPD-19147 + ETF-Oxidized + PROTON -> CPD-19161 + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadE (protein.Q47146). Substrates: H+ (molecule.C00080), (7Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD-19147). Products: (2E,7Z)-tetradec-2,7-enoyl-CoA (molecule.ecocyc.CPD-19161).

## Annotation

CPD-19147 + ETF-Oxidized + PROTON -> CPD-19161 + ETF-Reduced; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q47146|protein.Q47146]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-19161|molecule.ecocyc.CPD-19161]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19147|molecule.ecocyc.CPD-19147]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17792`

## Notes

CPD-19147 + ETF-Oxidized + PROTON -> CPD-19161 + ETF-Reduced; direction=REVERSIBLE
