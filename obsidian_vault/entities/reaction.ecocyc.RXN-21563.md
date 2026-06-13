---
entity_id: "reaction.ecocyc.RXN-21563"
entity_type: "reaction"
name: "RXN-21563"
source_database: "EcoCyc"
source_id: "RXN-21563"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21563

`reaction.ecocyc.RXN-21563`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21563`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-8122 + CPD-3 -> CPD-15870 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-8122 + CPD-3 -> CPD-15870 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by molybdopterin molybdotransferase (complex.ecocyc.CPLX0-8045). Substrates: Molybdate (molecule.C06232), Adenylated molybdopterin (molecule.C19848). Products: AMP (molecule.C00020), H+ (molecule.C00080), Molybdoenzyme molybdenum cofactor (molecule.C18237).

## Enriched Pathways

- `ecocyc.PWY-8171` molybdenum cofactor biosynthesis (EcoCyc)

## Annotation

CPD-8122 + CPD-3 -> CPD-15870 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8171` molybdenum cofactor biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8045|complex.ecocyc.CPLX0-8045]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06232|molecule.C06232]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C19848|molecule.C19848]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21563`

## Notes

CPD-8122 + CPD-3 -> CPD-15870 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
