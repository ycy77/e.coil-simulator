---
entity_id: "reaction.ecocyc.RXN-24038"
entity_type: "reaction"
name: "RXN-24038"
source_database: "EcoCyc"
source_id: "RXN-24038"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24038

`reaction.ecocyc.RXN-24038`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24038`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

BENZALDEHYDE + CPD-10145 + WATER -> BENZOATE + CPD-15487 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: BENZALDEHYDE + CPD-10145 + WATER -> BENZOATE + CPD-15487 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aldehyde dehydrogenase (complex.ecocyc.CPLX0-7805). Substrates: H2O (molecule.C00001), Benzaldehyde (molecule.C00261), ferricyanide (molecule.ecocyc.CPD-10145). Products: H+ (molecule.C00080), Benzoate (molecule.C00180), ferrocyanide (molecule.ecocyc.CPD-15487).

## Annotation

BENZALDEHYDE + CPD-10145 + WATER -> BENZOATE + CPD-15487 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7805|complex.ecocyc.CPLX0-7805]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00180|molecule.C00180]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15487|molecule.ecocyc.CPD-15487]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00261|molecule.C00261]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-10145|molecule.ecocyc.CPD-10145]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24038`

## Notes

BENZALDEHYDE + CPD-10145 + WATER -> BENZOATE + CPD-15487 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
