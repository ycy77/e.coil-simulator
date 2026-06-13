---
entity_id: "reaction.ecocyc.RXN-12195"
entity_type: "reaction"
name: "unspecific diphosphate phosphohydrolase"
source_database: "EcoCyc"
source_id: "RXN-12195"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# unspecific diphosphate phosphohydrolase

`reaction.ecocyc.RXN-12195`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12195`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + CTP -> PROTON + Pi + CDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + CTP -> PROTON + Pi + CDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), CTP (molecule.C00063). Products: H+ (molecule.C00080), CDP (molecule.C00112), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)

## Annotation

WATER + CTP -> PROTON + Pi + CDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00112|molecule.C00112]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12195`

## Notes

WATER + CTP -> PROTON + Pi + CDP; direction=PHYSIOL-LEFT-TO-RIGHT
