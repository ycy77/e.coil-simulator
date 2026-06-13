---
entity_id: "reaction.ecocyc.RXN-21026"
entity_type: "reaction"
name: "RXN-21026"
source_database: "EcoCyc"
source_id: "RXN-21026"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21026

`reaction.ecocyc.RXN-21026`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21026`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Thiarsahydroxy-SG-ArsC + Red-Glutaredoxins -> ArsC-S-As-OH + Grx-GSH-dithiol + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Thiarsahydroxy-SG-ArsC + Red-Glutaredoxins -> ArsC-S-As-OH + Grx-GSH-dithiol + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: S-glutathionyl-thiarsahydroxy-[arsenate reductase] (molecule.ecocyc.Thiarsahydroxy-SG-ArsC). Products: H2O (molecule.C00001), S-arsorososulfanethiol-[arsenate reductase] (molecule.ecocyc.ArsC-S-As-OH).

## Annotation

Thiarsahydroxy-SG-ArsC + Red-Glutaredoxins -> ArsC-S-As-OH + Grx-GSH-dithiol + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ArsC-S-As-OH|molecule.ecocyc.ArsC-S-As-OH]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Thiarsahydroxy-SG-ArsC|molecule.ecocyc.Thiarsahydroxy-SG-ArsC]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21026`

## Notes

Thiarsahydroxy-SG-ArsC + Red-Glutaredoxins -> ArsC-S-As-OH + Grx-GSH-dithiol + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
