---
entity_id: "reaction.ecocyc.RXN-15314"
entity_type: "reaction"
name: "N-acetylneuraminate:proton symport"
source_database: "EcoCyc"
source_id: "RXN-15314"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# N-acetylneuraminate:proton symport

`reaction.ecocyc.RXN-15314`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15314`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-1123 + PROTON -> CPD0-1123 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1123 + PROTON -> CPD0-1123 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by nanT (protein.P41036). Substrates: H+ (molecule.C00080), N-acetyl-β-neuraminate (molecule.ecocyc.CPD0-1123). Products: H+ (molecule.C00080), N-acetyl-β-neuraminate (molecule.ecocyc.CPD0-1123).

## Annotation

CPD0-1123 + PROTON -> CPD0-1123 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P41036|protein.P41036]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1123|molecule.ecocyc.CPD0-1123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1123|molecule.ecocyc.CPD0-1123]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15314`

## Notes

CPD0-1123 + PROTON -> CPD0-1123 + PROTON; direction=REVERSIBLE
