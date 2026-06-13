---
entity_id: "reaction.ecocyc.RXN0-7169"
entity_type: "reaction"
name: "RXN0-7169"
source_database: "EcoCyc"
source_id: "RXN0-7169"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7169

`reaction.ecocyc.RXN0-7169`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7169`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hpr-pi-phospho-L-histidines + DIHYDROXYACETONE -> Hpr-Histidine + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + DIHYDROXYACETONE -> Hpr-Histidine + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Glycerone (molecule.C00184), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: Glycerone phosphate (molecule.C00111), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + DIHYDROXYACETONE -> Hpr-Histidine + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00184|molecule.C00184]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7169`

## Notes

Hpr-pi-phospho-L-histidines + DIHYDROXYACETONE -> Hpr-Histidine + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
