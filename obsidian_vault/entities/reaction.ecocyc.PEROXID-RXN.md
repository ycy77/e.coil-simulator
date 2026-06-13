---
entity_id: "reaction.ecocyc.PEROXID-RXN"
entity_type: "reaction"
name: "PEROXID-RXN"
source_database: "EcoCyc"
source_id: "PEROXID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PEROXID-RXN

`reaction.ecocyc.PEROXID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PEROXID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC

## Enriched Summary

This reaction is involved in detoxification. EcoCyc reaction equation: Phenolic-Donors + HYDROGEN-PEROXIDE -> Phenoxyl-rad-of-phenolic-donors + WATER; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in detoxification.

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027), a phenolic donor (molecule.ecocyc.Phenolic-Donors). Products: H2O (molecule.C00001), a phenoxyl radical of a phenolic donor (molecule.ecocyc.Phenoxyl-rad-of-phenolic-donors).

## Annotation

This reaction is involved in detoxification.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Phenoxyl-rad-of-phenolic-donors|molecule.ecocyc.Phenoxyl-rad-of-phenolic-donors]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Phenolic-Donors|molecule.ecocyc.Phenolic-Donors]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PEROXID-RXN`

## Notes

Phenolic-Donors + HYDROGEN-PEROXIDE -> Phenoxyl-rad-of-phenolic-donors + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
