---
entity_id: "reaction.ecocyc.GLYOCARBOLIG-RXN"
entity_type: "reaction"
name: "GLYOCARBOLIG-RXN"
source_database: "EcoCyc"
source_id: "GLYOCARBOLIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYOCARBOLIG-RXN

`reaction.ecocyc.GLYOCARBOLIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYOCARBOLIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of glyoxylate catabolism. EcoCyc reaction equation: PROTON + GLYOX -> CPD-26279 + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of glyoxylate catabolism.

## Biological Role

Catalyzed by glyoxylate carboligase (complex.ecocyc.GLYOCARBOLIG-CPLX). Substrates: Glyoxylate (molecule.C00048), H+ (molecule.C00080). Products: CO2 (molecule.C00011), (2R)-tartronate semialdehyde (molecule.ecocyc.CPD-26279).

## Enriched Pathways

- `ecocyc.GLYCOLATEMET-PWY` glycolate and glyoxylate degradation I (EcoCyc)

## Annotation

This reaction is part of glyoxylate catabolism.

## Pathways

- `ecocyc.GLYCOLATEMET-PWY` glycolate and glyoxylate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.NH4CL|molecule.ecocyc.NH4CL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.SH-Compounds|molecule.ecocyc.SH-Compounds]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GLYOCARBOLIG-CPLX|complex.ecocyc.GLYOCARBOLIG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26279|molecule.ecocyc.CPD-26279]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1464|molecule.ecocyc.CPD0-1464]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.S2O4|molecule.ecocyc.S2O4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYOCARBOLIG-RXN`

## Notes

PROTON + GLYOX -> CPD-26279 + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
