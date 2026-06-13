---
entity_id: "reaction.ecocyc.TRANS-RXN0-258"
entity_type: "reaction"
name: "muropeptide:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-258"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# muropeptide:proton symport

`reaction.ecocyc.TRANS-RXN0-258`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-258`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD0-1081 -> PROTON + CPD0-1081; direction=REVERSIBLE EcoCyc reaction equation: PROTON + CPD0-1081 -> PROTON + CPD0-1081; direction=REVERSIBLE.

## Biological Role

Catalyzed by ampG (protein.P0AE16). Substrates: H+ (molecule.C00080), N-acetyl-β-D-glucosamine-1,6-anhydro-N-acetyl-β-D-muramate (molecule.ecocyc.CPD0-1081). Products: H+ (molecule.C00080), N-acetyl-β-D-glucosamine-1,6-anhydro-N-acetyl-β-D-muramate (molecule.ecocyc.CPD0-1081).

## Annotation

PROTON + CPD0-1081 -> PROTON + CPD0-1081; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AE16|protein.P0AE16]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1081|molecule.ecocyc.CPD0-1081]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1081|molecule.ecocyc.CPD0-1081]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-258`

## Notes

PROTON + CPD0-1081 -> PROTON + CPD0-1081; direction=REVERSIBLE
