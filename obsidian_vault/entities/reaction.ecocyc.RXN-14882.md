---
entity_id: "reaction.ecocyc.RXN-14882"
entity_type: "reaction"
name: "RXN-14882"
source_database: "EcoCyc"
source_id: "RXN-14882"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC|CCO-EXTRACELLULAR"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14882

`reaction.ecocyc.RXN-14882`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14882`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC|CCO-EXTRACELLULAR

## Enriched Summary

CPD-15818 -> D-Ribofuranose; direction=REVERSIBLE EcoCyc reaction equation: CPD-15818 -> D-Ribofuranose; direction=REVERSIBLE.

## Biological Role

Substrates: aldehydo-D-ribose (molecule.ecocyc.CPD-15818). Products: D-ribofuranose (molecule.ecocyc.D-Ribofuranose).

## Annotation

CPD-15818 -> D-Ribofuranose; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.D-Ribofuranose|molecule.ecocyc.D-Ribofuranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15818|molecule.ecocyc.CPD-15818]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14882`

## Notes

CPD-15818 -> D-Ribofuranose; direction=REVERSIBLE
