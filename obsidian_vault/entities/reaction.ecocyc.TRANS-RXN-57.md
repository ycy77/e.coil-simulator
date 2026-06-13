---
entity_id: "reaction.ecocyc.TRANS-RXN-57"
entity_type: "reaction"
name: "4-aminobutanoate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-57"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 4-aminobutanoate:proton symport

`reaction.ecocyc.TRANS-RXN-57`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-57`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + 4-AMINO-BUTYRATE -> PROTON + 4-AMINO-BUTYRATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + 4-AMINO-BUTYRATE -> PROTON + 4-AMINO-BUTYRATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by gabP (protein.P25527). Substrates: H+ (molecule.C00080), 4-Aminobutanoate (molecule.C00334). Products: H+ (molecule.C00080), 4-Aminobutanoate (molecule.C00334).

## Annotation

PROTON + 4-AMINO-BUTYRATE -> PROTON + 4-AMINO-BUTYRATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.NH42SO4|molecule.ecocyc.NH42SO4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P25527|protein.P25527]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00431|molecule.C00431]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-8179|molecule.ecocyc.CPD-8179]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-57`

## Notes

PROTON + 4-AMINO-BUTYRATE -> PROTON + 4-AMINO-BUTYRATE; direction=REVERSIBLE
