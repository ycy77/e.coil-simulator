---
entity_id: "reaction.ecocyc.BTUR2-RXN"
entity_type: "reaction"
name: "BTUR2-RXN"
source_database: "EcoCyc"
source_id: "BTUR2-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BTUR2-RXN

`reaction.ecocyc.BTUR2-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BTUR2-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CPD-20903 + Reduced-Flavoproteins -> ADENOSYLCOBINAMIDE + P3I + Oxidized-Flavoproteins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPD-20903 + Reduced-Flavoproteins -> ADENOSYLCOBINAMIDE + P3I + Oxidized-Flavoproteins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by btuR (protein.P0A9H5). Substrates: ATP (molecule.C00002), cob(II)inamide (molecule.ecocyc.CPD-20903). Products: Triphosphate (molecule.C00536), Adenosyl cobinamide (molecule.C06508).

## Annotation

ATP + CPD-20903 + Reduced-Flavoproteins -> ADENOSYLCOBINAMIDE + P3I + Oxidized-Flavoproteins; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9H5|protein.P0A9H5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00536|molecule.C00536]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06508|molecule.C06508]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20903|molecule.ecocyc.CPD-20903]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BTUR2-RXN`

## Notes

ATP + CPD-20903 + Reduced-Flavoproteins -> ADENOSYLCOBINAMIDE + P3I + Oxidized-Flavoproteins; direction=PHYSIOL-LEFT-TO-RIGHT
