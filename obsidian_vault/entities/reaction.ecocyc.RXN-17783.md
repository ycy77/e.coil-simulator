---
entity_id: "reaction.ecocyc.RXN-17783"
entity_type: "reaction"
name: "RXN-17783"
source_database: "EcoCyc"
source_id: "RXN-17783"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17783

`reaction.ecocyc.RXN-17783`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17783`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15436 + ETF-Oxidized + PROTON -> CPD0-1162 + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: CPD-15436 + ETF-Oxidized + PROTON -> CPD0-1162 + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadE (protein.Q47146). Substrates: H+ (molecule.C00080), (5Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD-15436). Products: (2E,5Z)-tetradec-2,5-enoyl-CoA (molecule.ecocyc.CPD0-1162).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-15436 + ETF-Oxidized + PROTON -> CPD0-1162 + ETF-Reduced; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q47146|protein.Q47146]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1162|molecule.ecocyc.CPD0-1162]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15436|molecule.ecocyc.CPD-15436]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17783`

## Notes

CPD-15436 + ETF-Oxidized + PROTON -> CPD0-1162 + ETF-Reduced; direction=REVERSIBLE
