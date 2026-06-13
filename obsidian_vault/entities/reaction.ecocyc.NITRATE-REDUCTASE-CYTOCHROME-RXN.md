---
entity_id: "reaction.ecocyc.NITRATE-REDUCTASE-CYTOCHROME-RXN"
entity_type: "reaction"
name: "NITRATE-REDUCTASE-CYTOCHROME-RXN"
source_database: "EcoCyc"
source_id: "NITRATE-REDUCTASE-CYTOCHROME-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NITRATE-REDUCTASE-CYTOCHROME-RXN

`reaction.ecocyc.NITRATE-REDUCTASE-CYTOCHROME-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NITRATE-REDUCTASE-CYTOCHROME-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Reduced-NapC-proteins + PROTON + NITRATE -> Oxidized-NapC-proteins + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Reduced-NapC-proteins + PROTON + NITRATE -> Oxidized-NapC-proteins + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by periplasmic nitrate reductase (complex.ecocyc.NAP-CPLX). Substrates: H+ (molecule.C00080), Nitrate (molecule.C00244). Products: H2O (molecule.C00001), Nitrite (molecule.C00088).

## Enriched Pathways

- `ecocyc.PWY0-1584` sn-glycerol 3-phosphate anaerobic respiration (EcoCyc)

## Annotation

Reduced-NapC-proteins + PROTON + NITRATE -> Oxidized-NapC-proteins + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1584` sn-glycerol 3-phosphate anaerobic respiration (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.NAP-CPLX|complex.ecocyc.NAP-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NITRATE-REDUCTASE-CYTOCHROME-RXN`

## Notes

Reduced-NapC-proteins + PROTON + NITRATE -> Oxidized-NapC-proteins + WATER + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT
