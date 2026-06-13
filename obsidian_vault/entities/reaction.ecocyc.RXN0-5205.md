---
entity_id: "reaction.ecocyc.RXN0-5205"
entity_type: "reaction"
name: "RXN0-5205"
source_database: "EcoCyc"
source_id: "RXN0-5205"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Zinc-translocating P-type ATPase"
  - "Zn(2+)-exporting ATPase"
---

# RXN0-5205

`reaction.ecocyc.RXN0-5205`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5205`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ZN+2 + WATER + ATP -> ZN+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ZN+2 + WATER + ATP -> ZN+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by zntA (protein.P37617). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Zinc cation (molecule.C00038). Products: ADP (molecule.C00008), Zinc cation (molecule.C00038), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

ZN+2 + WATER + ATP -> ZN+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P37617|protein.P37617]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5205`

## Notes

ZN+2 + WATER + ATP -> ZN+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
