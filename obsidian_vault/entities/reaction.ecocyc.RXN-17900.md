---
entity_id: "reaction.ecocyc.RXN-17900"
entity_type: "reaction"
name: "RXN-17900"
source_database: "EcoCyc"
source_id: "RXN-17900"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17900

`reaction.ecocyc.RXN-17900`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17900`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHOSPHORIBULOSYL-FORMIMINO-AICAR-P + AMMONIA -> D-ERYTHRO-IMIDAZOLE-GLYCEROL-P + AICAR + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHORIBULOSYL-FORMIMINO-AICAR-P + AMMONIA -> D-ERYTHRO-IMIDAZOLE-GLYCEROL-P + AICAR + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Ammonia (molecule.C00014), N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide (molecule.C04916). Products: H2O (molecule.C00001), D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate (molecule.C04666), 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide (molecule.C04677).

## Annotation

PHOSPHORIBULOSYL-FORMIMINO-AICAR-P + AMMONIA -> D-ERYTHRO-IMIDAZOLE-GLYCEROL-P + AICAR + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04666|molecule.C04666]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04677|molecule.C04677]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04916|molecule.C04916]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17900`

## Notes

PHOSPHORIBULOSYL-FORMIMINO-AICAR-P + AMMONIA -> D-ERYTHRO-IMIDAZOLE-GLYCEROL-P + AICAR + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
