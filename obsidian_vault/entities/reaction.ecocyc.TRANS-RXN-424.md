---
entity_id: "reaction.ecocyc.TRANS-RXN-424"
entity_type: "reaction"
name: "G protein coupled Fe2+ transport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-424"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# G protein coupled Fe2+ transport

`reaction.ecocyc.TRANS-RXN-424`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-424`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FE+2 + GTP + WATER -> FE+2 + GDP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FE+2 + GTP + WATER -> FE+2 + GDP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by feoB (protein.P33650). Substrates: H2O (molecule.C00001), GTP (molecule.C00044), Fe2+ (molecule.C14818). Products: GDP (molecule.C00035), H+ (molecule.C00080), Fe2+ (molecule.C14818), phosphate (molecule.ecocyc.Pi).

## Annotation

FE+2 + GTP + WATER -> FE+2 + GDP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P33650|protein.P33650]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-424`

## Notes

FE+2 + GTP + WATER -> FE+2 + GDP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
