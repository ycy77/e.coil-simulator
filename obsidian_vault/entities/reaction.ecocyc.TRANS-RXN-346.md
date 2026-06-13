---
entity_id: "reaction.ecocyc.TRANS-RXN-346"
entity_type: "reaction"
name: "Zn2+:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-346"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Zn2+:proton symport

`reaction.ecocyc.TRANS-RXN-346`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-346`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ZN+2 + PROTON -> ZN+2 + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ZN+2 + PROTON -> ZN+2 + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by zntB (protein.P64423). Substrates: Zinc cation (molecule.C00038), H+ (molecule.C00080). Products: Zinc cation (molecule.C00038), H+ (molecule.C00080).

## Annotation

ZN+2 + PROTON -> ZN+2 + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P64423|protein.P64423]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-346`

## Notes

ZN+2 + PROTON -> ZN+2 + PROTON; direction=LEFT-TO-RIGHT
