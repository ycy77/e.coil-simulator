---
entity_id: "reaction.ecocyc.RXN-22326"
entity_type: "reaction"
name: "RXN-22326"
source_database: "EcoCyc"
source_id: "RXN-22326"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22326

`reaction.ecocyc.RXN-22326`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22326`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ARSENATE + ATP + WATER -> ARSENATE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ARSENATE + ATP + WATER -> ARSENATE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phosphate ABC transporter (complex.ecocyc.ABC-27-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), arsenate (molecule.ecocyc.ARSENATE). Products: ADP (molecule.C00008), H+ (molecule.C00080), arsenate (molecule.ecocyc.ARSENATE), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-4621-1` arsenic detoxification VI (E. coli) (EcoCyc)

## Annotation

ARSENATE + ATP + WATER -> ARSENATE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-4621-1` arsenic detoxification VI (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-27-CPLX|complex.ecocyc.ABC-27-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22326`

## Notes

ARSENATE + ATP + WATER -> ARSENATE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
