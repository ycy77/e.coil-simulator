---
entity_id: "reaction.ecocyc.TRANS-RXN-41"
entity_type: "reaction"
name: "fosmidomycin:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-41"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# fosmidomycin:proton antiport

`reaction.ecocyc.TRANS-RXN-41`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-41`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-441 + PROTON -> CPD0-441 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-441 + PROTON -> CPD0-441 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by fsr (protein.P52067). Substrates: H+ (molecule.C00080), fosmidomycin (molecule.ecocyc.CPD0-441). Products: H+ (molecule.C00080), fosmidomycin (molecule.ecocyc.CPD0-441).

## Annotation

CPD0-441 + PROTON -> CPD0-441 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P52067|protein.P52067]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-441|molecule.ecocyc.CPD0-441]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-441|molecule.ecocyc.CPD0-441]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-41`

## Notes

CPD0-441 + PROTON -> CPD0-441 + PROTON; direction=REVERSIBLE
