---
entity_id: "reaction.ecocyc.RXN0-5507"
entity_type: "reaction"
name: "RXN0-5507"
source_database: "EcoCyc"
source_id: "RXN0-5507"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5507

`reaction.ecocyc.RXN0-5507`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5507`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDRONEOPTERIN-P3 + WATER -> CPD0-1699 + ACETALD + P3I + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DIHYDRONEOPTERIN-P3 + WATER -> CPD0-1699 + ACETALD + P3I + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 6-carboxy-5,6,7,8-tetrahydropterin synthase (complex.ecocyc.CPLX0-8123). Substrates: H2O (molecule.C00001), 7,8-Dihydroneopterin 3'-triphosphate (molecule.C04895). Products: H+ (molecule.C00080), Acetaldehyde (molecule.C00084), Triphosphate (molecule.C00536), 6-Carboxy-5,6,7,8-tetrahydropterin (molecule.C20239).

## Enriched Pathways

- `ecocyc.PWY-6703` preQ0 biosynthesis (EcoCyc)

## Annotation

DIHYDRONEOPTERIN-P3 + WATER -> CPD0-1699 + ACETALD + P3I + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6703` preQ0 biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8123|complex.ecocyc.CPLX0-8123]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00536|molecule.C00536]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20239|molecule.C20239]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04895|molecule.C04895]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5507`

## Notes

DIHYDRONEOPTERIN-P3 + WATER -> CPD0-1699 + ACETALD + P3I + PROTON; direction=LEFT-TO-RIGHT
