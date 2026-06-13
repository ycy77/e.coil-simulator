---
entity_id: "reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN"
entity_type: "reaction"
name: "SUCCINYLDIAMINOPIMTRANS-RXN"
source_database: "EcoCyc"
source_id: "SUCCINYLDIAMINOPIMTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUCCINYLDIAMINOPIMTRANS-RXN

`reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCINYLDIAMINOPIMTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth step in the biosynthesis of diaminopimelate and lysine from aspartate semialdehyde. EcoCyc reaction equation: 2-KETOGLUTARATE + N-SUCCINYLLL-2-6-DIAMINOPIMELATE -> GLT + N-SUCCINYL-2-AMINO-6-KETOPIMELATE; direction=REVERSIBLE. This is the fourth step in the biosynthesis of diaminopimelate and lysine from aspartate semialdehyde.

## Biological Role

Catalyzed by N-acetylornithine aminotransferase / N-succinyldiaminopimelate aminotransferase (complex.ecocyc.ACETYLORNTRANSAM-CPLX), phosphoserine/phosphohydroxythreonine aminotransferase (complex.ecocyc.PSERTRANSAM-CPLX). Substrates: 2-Oxoglutarate (molecule.C00026), N-Succinyl-LL-2,6-diaminoheptanedioate (molecule.C04421). Products: L-Glutamate (molecule.C00025), N-Succinyl-2-L-amino-6-oxoheptanedioate (molecule.C04462).

## Enriched Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Annotation

This is the fourth step in the biosynthesis of diaminopimelate and lysine from aspartate semialdehyde.

## Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ACETYLORNTRANSAM-CPLX|complex.ecocyc.ACETYLORNTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.PSERTRANSAM-CPLX|complex.ecocyc.PSERTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04462|molecule.C04462]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04421|molecule.C04421]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SUCCINYLDIAMINOPIMTRANS-RXN`

## Notes

2-KETOGLUTARATE + N-SUCCINYLLL-2-6-DIAMINOPIMELATE -> GLT + N-SUCCINYL-2-AMINO-6-KETOPIMELATE; direction=REVERSIBLE
