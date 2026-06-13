---
entity_id: "reaction.ecocyc.RXN0-3501"
entity_type: "reaction"
name: "RXN0-3501"
source_database: "EcoCyc"
source_id: "RXN0-3501"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3501

`reaction.ecocyc.RXN0-3501`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3501`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinols + NITRATE + PROTON -> Menaquinones + NITRITE + WATER + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Menaquinols + NITRATE + PROTON -> Menaquinones + NITRITE + WATER + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nitrate reductase A (complex.ecocyc.NITRATREDUCTA-CPLX), nitrate reductase Z (complex.ecocyc.NITRATREDUCTZ-CPLX). Substrates: H+ (molecule.C00080), Nitrate (molecule.C00244), Menaquinol (molecule.C05819). Products: H2O (molecule.C00001), H+ (molecule.C00080), Nitrite (molecule.C00088), Menaquinone (molecule.C00828).

## Enriched Pathways

- `ecocyc.PWY0-1321` nitrate reduction III (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1352` nitrate reduction VIII (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1581` nitrate reduction IX (dissimilatory) (EcoCyc)

## Annotation

Menaquinols + NITRATE + PROTON -> Menaquinones + NITRITE + WATER + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1321` nitrate reduction III (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1352` nitrate reduction VIII (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1581` nitrate reduction IX (dissimilatory) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[complex.ecocyc.NITRATREDUCTA-CPLX|complex.ecocyc.NITRATREDUCTA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.NITRATREDUCTZ-CPLX|complex.ecocyc.NITRATREDUCTZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13584|molecule.ecocyc.CPD-13584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2841|molecule.ecocyc.CPD-2841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7975|molecule.ecocyc.CPD-7975]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1686|molecule.ecocyc.CPD0-1686]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-3501`

## Notes

Menaquinols + NITRATE + PROTON -> Menaquinones + NITRITE + WATER + PROTON; direction=LEFT-TO-RIGHT
