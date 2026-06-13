---
entity_id: "reaction.ecocyc.RXN-22385"
entity_type: "reaction"
name: "RXN-22385"
source_database: "EcoCyc"
source_id: "RXN-22385"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22385

`reaction.ecocyc.RXN-22385`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22385`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD0-2040 -> PROTON + CPD0-2040; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD0-2040 -> PROTON + CPD0-2040; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by arsenite/antimonite:H+ antiporter (complex.ecocyc.CPLX-7). Substrates: H+ (molecule.C00080), arsenous acid (molecule.ecocyc.CPD0-2040). Products: H+ (molecule.C00080), arsenous acid (molecule.ecocyc.CPD0-2040).

## Enriched Pathways

- `ecocyc.PWY-4621-1` arsenic detoxification VI (E. coli) (EcoCyc)

## Annotation

PROTON + CPD0-2040 -> PROTON + CPD0-2040; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-4621-1` arsenic detoxification VI (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-7|complex.ecocyc.CPLX-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2040|molecule.ecocyc.CPD0-2040]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2040|molecule.ecocyc.CPD0-2040]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22385`

## Notes

PROTON + CPD0-2040 -> PROTON + CPD0-2040; direction=LEFT-TO-RIGHT
