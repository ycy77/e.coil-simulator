---
entity_id: "reaction.ecocyc.TRANS-RXN-132"
entity_type: "reaction"
name: "uracil:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-132"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# uracil:proton symport

`reaction.ecocyc.TRANS-RXN-132`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-132`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + URACIL -> PROTON + URACIL; direction=REVERSIBLE EcoCyc reaction equation: PROTON + URACIL -> PROTON + URACIL; direction=REVERSIBLE.

## Biological Role

Catalyzed by uracil transporter UraA (complex.ecocyc.CPLX0-8247), rutG (protein.P75892). Substrates: H+ (molecule.C00080), Uracil (molecule.C00106). Products: H+ (molecule.C00080), Uracil (molecule.C00106).

## Annotation

PROTON + URACIL -> PROTON + URACIL; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8247|complex.ecocyc.CPLX0-8247]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75892|protein.P75892]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00380|molecule.C00380]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-21304|molecule.ecocyc.CPD-21304]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1327|molecule.ecocyc.CPD0-1327]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-132`

## Notes

PROTON + URACIL -> PROTON + URACIL; direction=REVERSIBLE
