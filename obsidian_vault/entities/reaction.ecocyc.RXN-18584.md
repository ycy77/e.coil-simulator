---
entity_id: "reaction.ecocyc.RXN-18584"
entity_type: "reaction"
name: "RXN-18584"
source_database: "EcoCyc"
source_id: "RXN-18584"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18584

`reaction.ecocyc.RXN-18584`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18584`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Ubiquinols + Oxidized-NapC-proteins -> Ubiquinones + PROTON + Reduced-NapC-proteins; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Ubiquinols + Oxidized-NapC-proteins -> Ubiquinones + PROTON + Reduced-NapC-proteins; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ubiquinol—[NapC cytochrome c] reductase (complex.ecocyc.CPLX0-3241). Substrates: Ubiquinol (molecule.C00390). Products: H+ (molecule.C00080), a ubiquinone (molecule.ecocyc.Ubiquinones).

## Enriched Pathways

- `ecocyc.PWY0-1584` sn-glycerol 3-phosphate anaerobic respiration (EcoCyc)

## Annotation

Ubiquinols + Oxidized-NapC-proteins -> Ubiquinones + PROTON + Reduced-NapC-proteins; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1584` sn-glycerol 3-phosphate anaerobic respiration (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3241|complex.ecocyc.CPLX0-3241]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18584`

## Notes

Ubiquinols + Oxidized-NapC-proteins -> Ubiquinones + PROTON + Reduced-NapC-proteins; direction=LEFT-TO-RIGHT
