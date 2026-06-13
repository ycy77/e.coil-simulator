---
entity_id: "reaction.ecocyc.MHPCHYDROL-RXN"
entity_type: "reaction"
name: "MHPCHYDROL-RXN"
source_database: "EcoCyc"
source_id: "MHPCHYDROL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MHPCHYDROL-RXN

`reaction.ecocyc.MHPCHYDROL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MHPCHYDROL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate. EcoCyc reaction equation: CPD-157 + WATER -> CPD-14447 + SUC + PROTON; direction=LEFT-TO-RIGHT. This is the fifth reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate.

## Biological Role

Catalyzed by 2-hydroxy-6-oxononatrienedioate hydrolase (complex.ecocyc.CPLX0-7950). Substrates: H2O (molecule.C00001), 2-Hydroxy-6-oxonona-2,4-diene-1,9-dioate (molecule.C04479). Products: Succinate (molecule.C00042), H+ (molecule.C00080), (2Z)-2-hydroxypenta-2,4-dienoate (molecule.ecocyc.CPD-14447).

## Enriched Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

This is the fifth reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate.

## Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7950|complex.ecocyc.CPLX0-7950]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-14447|molecule.ecocyc.CPD-14447]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04479|molecule.C04479]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MHPCHYDROL-RXN`

## Notes

CPD-157 + WATER -> CPD-14447 + SUC + PROTON; direction=LEFT-TO-RIGHT
