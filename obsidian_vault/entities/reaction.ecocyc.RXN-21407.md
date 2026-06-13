---
entity_id: "reaction.ecocyc.RXN-21407"
entity_type: "reaction"
name: "RXN-21407"
source_database: "EcoCyc"
source_id: "RXN-21407"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21407

`reaction.ecocyc.RXN-21407`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21407`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTOHEME + CcmCDE-Complex + Acceptor + PROTON -> CcmCDE-Complex-Heme + Donor-H1; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTOHEME + CcmCDE-Complex + Acceptor + PROTON -> CcmCDE-Complex-Heme + Donor-H1; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by CcmCDE complex (complex.ecocyc.ABC-35-CPLX). Substrates: H+ (molecule.C00080), protoheme (molecule.ecocyc.PROTOHEME).

## Enriched Pathways

- `ecocyc.PWY-8147` cytochrome c biogenesis (system I type) (EcoCyc)

## Annotation

PROTOHEME + CcmCDE-Complex + Acceptor + PROTON -> CcmCDE-Complex-Heme + Donor-H1; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8147` cytochrome c biogenesis (system I type) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.ABC-35-CPLX|complex.ecocyc.ABC-35-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROTOHEME|molecule.ecocyc.PROTOHEME]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21407`

## Notes

PROTOHEME + CcmCDE-Complex + Acceptor + PROTON -> CcmCDE-Complex-Heme + Donor-H1; direction=PHYSIOL-LEFT-TO-RIGHT
