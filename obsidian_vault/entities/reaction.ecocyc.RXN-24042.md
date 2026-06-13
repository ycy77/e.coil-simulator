---
entity_id: "reaction.ecocyc.RXN-24042"
entity_type: "reaction"
name: "RXN-24042"
source_database: "EcoCyc"
source_id: "RXN-24042"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24042

`reaction.ecocyc.RXN-24042`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24042`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CINNAMALDEHYDE + CPD-10145 + WATER -> CPD-674 + CPD-15487 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CINNAMALDEHYDE + CPD-10145 + WATER -> CPD-674 + CPD-15487 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aldehyde dehydrogenase (complex.ecocyc.CPLX0-7805). Substrates: H2O (molecule.C00001), cinnamaldehyde (molecule.ecocyc.CINNAMALDEHYDE), ferricyanide (molecule.ecocyc.CPD-10145). Products: H+ (molecule.C00080), trans-Cinnamate (molecule.C00423), ferrocyanide (molecule.ecocyc.CPD-15487).

## Annotation

CINNAMALDEHYDE + CPD-10145 + WATER -> CPD-674 + CPD-15487 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7805|complex.ecocyc.CPLX0-7805]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00423|molecule.C00423]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15487|molecule.ecocyc.CPD-15487]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CINNAMALDEHYDE|molecule.ecocyc.CINNAMALDEHYDE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-10145|molecule.ecocyc.CPD-10145]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24042`

## Notes

CINNAMALDEHYDE + CPD-10145 + WATER -> CPD-674 + CPD-15487 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
