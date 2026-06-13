---
entity_id: "reaction.ecocyc.RXN-8342"
entity_type: "reaction"
name: "RXN-8342"
source_database: "EcoCyc"
source_id: "RXN-8342"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8342

`reaction.ecocyc.RXN-8342`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8342`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PRECURSOR-Z + Thiocarboxylated-MPT-synthases + WATER -> CPD-4 + MPT-Synthase-small-subunits + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PRECURSOR-Z + Thiocarboxylated-MPT-synthases + WATER -> CPD-4 + MPT-Synthase-small-subunits + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by molybdopterin synthase (complex.ecocyc.CPLX0-2502). Substrates: H2O (molecule.C00001), cyclic pyranopterin phosphate (molecule.ecocyc.PRECURSOR-Z). Products: H+ (molecule.C00080), Molybdopterin (molecule.C05924).

## Enriched Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Annotation

PRECURSOR-Z + Thiocarboxylated-MPT-synthases + WATER -> CPD-4 + MPT-Synthase-small-subunits + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2502|complex.ecocyc.CPLX0-2502]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05924|molecule.C05924]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PRECURSOR-Z|molecule.ecocyc.PRECURSOR-Z]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8342`

## Notes

PRECURSOR-Z + Thiocarboxylated-MPT-synthases + WATER -> CPD-4 + MPT-Synthase-small-subunits + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
