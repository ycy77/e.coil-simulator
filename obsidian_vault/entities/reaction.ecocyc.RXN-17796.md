---
entity_id: "reaction.ecocyc.RXN-17796"
entity_type: "reaction"
name: "RXN-17796"
source_database: "EcoCyc"
source_id: "RXN-17796"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17796

`reaction.ecocyc.RXN-17796`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17796`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19148 + ETF-Oxidized + PROTON -> CPD-19150 + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: CPD-19148 + ETF-Oxidized + PROTON -> CPD-19150 + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadE (protein.Q47146). Substrates: H+ (molecule.C00080), (5Z)-dodecenoyl-CoA (molecule.ecocyc.CPD-19148). Products: (2E,5Z)-dodec-2,5-dienoyl-CoA (molecule.ecocyc.CPD-19150).

## Annotation

CPD-19148 + ETF-Oxidized + PROTON -> CPD-19150 + ETF-Reduced; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q47146|protein.Q47146]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-19150|molecule.ecocyc.CPD-19150]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19148|molecule.ecocyc.CPD-19148]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17796`

## Notes

CPD-19148 + ETF-Oxidized + PROTON -> CPD-19150 + ETF-Reduced; direction=REVERSIBLE
