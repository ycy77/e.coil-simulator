---
entity_id: "reaction.ecocyc.TRANS-RXN0-486"
entity_type: "reaction"
name: "TRANS-RXN0-486"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-486"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-486

`reaction.ecocyc.TRANS-RXN0-486`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-486`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-397 -> CPD-397; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-397 -> CPD-397; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mmuP (protein.Q47689). Substrates: S-Methyl-L-methionine (molecule.C03172). Products: S-Methyl-L-methionine (molecule.C03172).

## Annotation

CPD-397 -> CPD-397; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.Q47689|protein.Q47689]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03172|molecule.C03172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03172|molecule.C03172]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-486`

## Notes

CPD-397 -> CPD-397; direction=PHYSIOL-LEFT-TO-RIGHT
