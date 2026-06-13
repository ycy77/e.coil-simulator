---
entity_id: "reaction.ecocyc.TRANS-RXN0-519"
entity_type: "reaction"
name: "α-methylgalactoside:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-519"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# α-methylgalactoside:proton symport

`reaction.ecocyc.TRANS-RXN0-519`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-519`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-3565 + PROTON -> CPD-3565 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-3565 + PROTON -> CPD-3565 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by melB (protein.P02921). Substrates: H+ (molecule.C00080), methyl-α-D-galactopyranoside (molecule.ecocyc.CPD-3565). Products: H+ (molecule.C00080), methyl-α-D-galactopyranoside (molecule.ecocyc.CPD-3565).

## Annotation

CPD-3565 + PROTON -> CPD-3565 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P02921|protein.P02921]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-3565|molecule.ecocyc.CPD-3565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3565|molecule.ecocyc.CPD-3565]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-519`

## Notes

CPD-3565 + PROTON -> CPD-3565 + PROTON; direction=REVERSIBLE
