---
entity_id: "reaction.ecocyc.OROTPDECARB-RXN"
entity_type: "reaction"
name: "OROTPDECARB-RXN"
source_database: "EcoCyc"
source_id: "OROTPDECARB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# OROTPDECARB-RXN

`reaction.ecocyc.OROTPDECARB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OROTPDECARB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the sixth and final step in the biosynthesis of pyrimidine. EcoCyc reaction equation: PROTON + OROTIDINE-5-PHOSPHATE -> CARBON-DIOXIDE + UMP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the sixth and final step in the biosynthesis of pyrimidine.

## Biological Role

Catalyzed by orotidine-5'-phosphate decarboxylase (complex.ecocyc.OROTPDECARB-CPLX). Substrates: H+ (molecule.C00080), Orotidine 5'-phosphate (molecule.C01103). Products: CO2 (molecule.C00011), UMP (molecule.C00105).

## Enriched Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Annotation

This is the sixth and final step in the biosynthesis of pyrimidine.

## Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.OROTPDECARB-CPLX|complex.ecocyc.OROTPDECARB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01103|molecule.C01103]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-2358|molecule.ecocyc.CPD0-2358]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:OROTPDECARB-RXN`

## Notes

PROTON + OROTIDINE-5-PHOSPHATE -> CARBON-DIOXIDE + UMP; direction=PHYSIOL-LEFT-TO-RIGHT
