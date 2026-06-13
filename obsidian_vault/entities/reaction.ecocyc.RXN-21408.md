---
entity_id: "reaction.ecocyc.RXN-21408"
entity_type: "reaction"
name: "RXN-21408"
source_database: "EcoCyc"
source_id: "RXN-21408"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21408

`reaction.ecocyc.RXN-21408`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21408`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CcmAB-Complex + CcmCDE-Complex-Heme -> CcmABCD-Complex + CcmE-Protein-Heme + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CcmAB-Complex + CcmCDE-Complex-Heme -> CcmABCD-Complex + CcmE-Protein-Heme + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by CcmAB (complex.ecocyc.CPLX-9493). Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-8147` cytochrome c biogenesis (system I type) (EcoCyc)

## Annotation

ATP + CcmAB-Complex + CcmCDE-Complex-Heme -> CcmABCD-Complex + CcmE-Protein-Heme + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8147` cytochrome c biogenesis (system I type) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX-9493|complex.ecocyc.CPLX-9493]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21408`

## Notes

ATP + CcmAB-Complex + CcmCDE-Complex-Heme -> CcmABCD-Complex + CcmE-Protein-Heme + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
