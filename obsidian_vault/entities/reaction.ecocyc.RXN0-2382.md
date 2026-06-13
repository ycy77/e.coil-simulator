---
entity_id: "reaction.ecocyc.RXN0-2382"
entity_type: "reaction"
name: "RXN0-2382"
source_database: "EcoCyc"
source_id: "RXN0-2382"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2382

`reaction.ecocyc.RXN0-2382`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2382`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

INDOLE + SER -> TRP + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: INDOLE + SER -> TRP + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tryptophan synthase, β subunit dimer (complex.ecocyc.CPLX0-2401). Substrates: L-Serine (molecule.C00065), Indole (molecule.C00463). Products: H2O (molecule.C00001), L-Tryptophan (molecule.C00078).

## Enriched Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Annotation

INDOLE + SER -> TRP + WATER; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2401|complex.ecocyc.CPLX0-2401]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00463|molecule.C00463]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2382`

## Notes

INDOLE + SER -> TRP + WATER; direction=LEFT-TO-RIGHT
