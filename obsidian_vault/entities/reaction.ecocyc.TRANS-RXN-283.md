---
entity_id: "reaction.ecocyc.TRANS-RXN-283"
entity_type: "reaction"
name: "TRANS-RXN-283"
source_database: "EcoCyc"
source_id: "TRANS-RXN-283"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-283

`reaction.ecocyc.TRANS-RXN-283`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-283`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

BETAINE + ATP + WATER -> BETAINE + Pi + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: BETAINE + ATP + WATER -> BETAINE + Pi + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glycine betaine ABC transporter, non-osmoregulatory (complex.ecocyc.ABC-40-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Betaine (molecule.C00719). Products: ADP (molecule.C00008), H+ (molecule.C00080), Betaine (molecule.C00719), phosphate (molecule.ecocyc.Pi).

## Annotation

BETAINE + ATP + WATER -> BETAINE + Pi + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-40-CPLX|complex.ecocyc.ABC-40-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-283`

## Notes

BETAINE + ATP + WATER -> BETAINE + Pi + PROTON + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
