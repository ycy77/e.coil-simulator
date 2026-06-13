---
entity_id: "reaction.ecocyc.TRNA-CYTIDYLYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "TRNA-CYTIDYLYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "TRNA-CYTIDYLYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "tRNA CCA-pyrophosphorylase"
  - "tRNA CCA-diphosphorylase"
---

# TRNA-CYTIDYLYLTRANSFERASE-RXN

`reaction.ecocyc.TRNA-CYTIDYLYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRNA-CYTIDYLYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-precursors + CTP + ATP -> tRNAs-with-CCA + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-precursors + CTP + ATP -> tRNAs-with-CCA + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cca (protein.P06961). Substrates: ATP (molecule.C00002), CTP (molecule.C00063). Products: Diphosphate (molecule.C00013).

## Annotation

tRNA-precursors + CTP + ATP -> tRNAs-with-CCA + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P06961|protein.P06961]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRNA-CYTIDYLYLTRANSFERASE-RXN`

## Notes

tRNA-precursors + CTP + ATP -> tRNAs-with-CCA + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
