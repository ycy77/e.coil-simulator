---
entity_id: "reaction.ecocyc.RXN-8344"
entity_type: "reaction"
name: "RXN-8344"
source_database: "EcoCyc"
source_id: "RXN-8344"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8344

`reaction.ecocyc.RXN-8344`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8344`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + CPD-4 + ATP -> CPD-8122 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD-4 + ATP -> CPD-8122 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by molybdopterin adenylyltransferase (complex.ecocyc.CPLX0-8163). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), Molybdopterin (molecule.C05924). Products: Diphosphate (molecule.C00013), Adenylated molybdopterin (molecule.C19848).

## Enriched Pathways

- `ecocyc.PWY-8171` molybdenum cofactor biosynthesis (EcoCyc)

## Annotation

PROTON + CPD-4 + ATP -> CPD-8122 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8171` molybdenum cofactor biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8163|complex.ecocyc.CPLX0-8163]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C19848|molecule.C19848]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05924|molecule.C05924]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8344`

## Notes

PROTON + CPD-4 + ATP -> CPD-8122 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
