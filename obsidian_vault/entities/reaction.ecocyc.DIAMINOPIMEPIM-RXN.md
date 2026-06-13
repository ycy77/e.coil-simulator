---
entity_id: "reaction.ecocyc.DIAMINOPIMEPIM-RXN"
entity_type: "reaction"
name: "DIAMINOPIMEPIM-RXN"
source_database: "EcoCyc"
source_id: "DIAMINOPIMEPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIAMINOPIMEPIM-RXN

`reaction.ecocyc.DIAMINOPIMEPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIAMINOPIMEPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the sixth and last step in the synthesis of diaminopimelate, and the penultimate step in the synthesis of lysine. EcoCyc reaction equation: LL-DIAMINOPIMELATE -> MESO-DIAMINOPIMELATE; direction=REVERSIBLE. This is the sixth and last step in the synthesis of diaminopimelate, and the penultimate step in the synthesis of lysine.

## Biological Role

Catalyzed by diaminopimelate epimerase (complex.ecocyc.CPLX0-7997). Substrates: LL-2,6-Diaminoheptanedioate (molecule.C00666). Products: meso-2,6-Diaminoheptanedioate (molecule.C00680).

## Enriched Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Annotation

This is the sixth and last step in the synthesis of diaminopimelate, and the penultimate step in the synthesis of lysine.

## Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7997|complex.ecocyc.CPLX0-7997]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00680|molecule.C00680]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00666|molecule.C00666]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1498|molecule.ecocyc.CPD0-1498]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1499|molecule.ecocyc.CPD0-1499]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1500|molecule.ecocyc.CPD0-1500]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1501|molecule.ecocyc.CPD0-1501]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1502|molecule.ecocyc.CPD0-1502]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1530|molecule.ecocyc.CPD0-1530]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1532|molecule.ecocyc.CPD0-1532]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1533|molecule.ecocyc.CPD0-1533]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1535|molecule.ecocyc.CPD0-1535]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1536|molecule.ecocyc.CPD0-1536]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1537|molecule.ecocyc.CPD0-1537]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Lanthionine-Isomers|molecule.ecocyc.Lanthionine-Isomers]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIAMINOPIMEPIM-RXN`

## Notes

LL-DIAMINOPIMELATE -> MESO-DIAMINOPIMELATE; direction=REVERSIBLE
