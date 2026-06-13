---
entity_id: "reaction.ecocyc.RXN-8001"
entity_type: "reaction"
name: "RXN-8001"
source_database: "EcoCyc"
source_id: "RXN-8001"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8001

`reaction.ecocyc.RXN-8001`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8001`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HISTIDINOL + NAD + WATER -> HIS + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HISTIDINOL + NAD + WATER -> HIS + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by histidinol dehydrogenase (complex.ecocyc.HISTDEHYD-CPLX). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), L-Histidinol (molecule.C00860). Products: NADH (molecule.C00004), H+ (molecule.C00080), L-Histidine (molecule.C00135).

## Annotation

HISTIDINOL + NAD + WATER -> HIS + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.HISTDEHYD-CPLX|complex.ecocyc.HISTDEHYD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00135|molecule.C00135]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00860|molecule.C00860]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8001`

## Notes

HISTIDINOL + NAD + WATER -> HIS + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
