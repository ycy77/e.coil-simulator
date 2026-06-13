---
entity_id: "reaction.ecocyc.RXN-12002"
entity_type: "reaction"
name: "RXN-12002"
source_database: "EcoCyc"
source_id: "RXN-12002"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12002

`reaction.ecocyc.RXN-12002`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12002`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + UMP -> ADP + UDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + UMP -> ADP + UDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by UMP kinase (complex.ecocyc.UMPKI-CPLX). Substrates: ATP (molecule.C00002), UMP (molecule.C00105). Products: ADP (molecule.C00008), UDP (molecule.C00015).

## Enriched Pathways

- `ecocyc.PWY-7176` UTP and CTP de novo biosynthesis (EcoCyc)

## Annotation

ATP + UMP -> ADP + UDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7176` UTP and CTP de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.UMPKI-CPLX|complex.ecocyc.UMPKI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-12002`

## Notes

ATP + UMP -> ADP + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
