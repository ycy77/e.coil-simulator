---
entity_id: "reaction.ecocyc.RXN0-6938"
entity_type: "reaction"
name: "RXN0-6938"
source_database: "EcoCyc"
source_id: "RXN0-6938"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6938

`reaction.ecocyc.RXN0-6938`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6938`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FERRIC-ENTEROBACTIN-COMPLEX + WATER -> CPD0-2482 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FERRIC-ENTEROBACTIN-COMPLEX + WATER -> CPD0-2482 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fes (protein.P13039). Substrates: H2O (molecule.C00001), Fe-enterobactin (molecule.C06230). Products: H+ (molecule.C00080), iron(III)-[N-(2,3-dihydroxybenzoyl)-L-serine trimer] complex (molecule.ecocyc.CPD0-2482).

## Annotation

FERRIC-ENTEROBACTIN-COMPLEX + WATER -> CPD0-2482 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P13039|protein.P13039]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2482|molecule.ecocyc.CPD0-2482]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06230|molecule.C06230]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6938`

## Notes

FERRIC-ENTEROBACTIN-COMPLEX + WATER -> CPD0-2482 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
