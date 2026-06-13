---
entity_id: "reaction.ecocyc.TRANS-RXN0-200"
entity_type: "reaction"
name: "Zn2+:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-200"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Zn2+:proton antiport

`reaction.ecocyc.TRANS-RXN0-200`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-200`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + ZN+2 -> PROTON + ZN+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + ZN+2 -> PROTON + ZN+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by Zn2+/Fe2+/Cd2+ exporter (complex.ecocyc.CPLX0-7641), zitB (protein.P75757). Substrates: Zinc cation (molecule.C00038), H+ (molecule.C00080). Products: Zinc cation (molecule.C00038), H+ (molecule.C00080).

## Annotation

PROTON + ZN+2 -> PROTON + ZN+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7641|complex.ecocyc.CPLX0-7641]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75757|protein.P75757]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-200`

## Notes

PROTON + ZN+2 -> PROTON + ZN+2; direction=LEFT-TO-RIGHT
