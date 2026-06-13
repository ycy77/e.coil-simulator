---
entity_id: "reaction.ecocyc.RXN0-11"
entity_type: "reaction"
name: "RXN0-11"
source_database: "EcoCyc"
source_id: "RXN0-11"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-11

`reaction.ecocyc.RXN0-11`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-11`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GLUTATHIONE + ATP + WATER -> GLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTATHIONE + ATP + WATER -> GLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by oligopeptide ABC transporter (complex.ecocyc.ABC-22-CPLX), glutathione ABC transporter (complex.ecocyc.ABC-49-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Glutathione (molecule.C00051). Products: ADP (molecule.C00008), Glutathione (molecule.C00051), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

GLUTATHIONE + ATP + WATER -> GLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ABC-22-CPLX|complex.ecocyc.ABC-22-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ABC-49-CPLX|complex.ecocyc.ABC-49-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-11`

## Notes

GLUTATHIONE + ATP + WATER -> GLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
