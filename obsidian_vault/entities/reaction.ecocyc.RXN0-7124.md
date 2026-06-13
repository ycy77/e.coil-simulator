---
entity_id: "reaction.ecocyc.RXN0-7124"
entity_type: "reaction"
name: "RXN0-7124"
source_database: "EcoCyc"
source_id: "RXN0-7124"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7124

`reaction.ecocyc.RXN0-7124`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7124`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Ubiquinols + PROTON + NITRATE -> Ubiquinones + PROTON + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Ubiquinols + PROTON + NITRATE -> Ubiquinones + PROTON + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nitrate reductase A (complex.ecocyc.NITRATREDUCTA-CPLX). Substrates: H+ (molecule.C00080), Nitrate (molecule.C00244), Ubiquinol (molecule.C00390). Products: H2O (molecule.C00001), H+ (molecule.C00080), Nitrite (molecule.C00088), a ubiquinone (molecule.ecocyc.Ubiquinones).

## Enriched Pathways

- `ecocyc.PWY0-1573` nitrate reduction VIIIb (dissimilatory) (EcoCyc)

## Annotation

Ubiquinols + PROTON + NITRATE -> Ubiquinones + PROTON + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1573` nitrate reduction VIIIb (dissimilatory) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.NITRATREDUCTA-CPLX|complex.ecocyc.NITRATREDUCTA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7124`

## Notes

Ubiquinols + PROTON + NITRATE -> Ubiquinones + PROTON + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT
