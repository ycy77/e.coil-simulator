---
entity_id: "reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN"
entity_type: "reaction"
name: "EXOPOLYPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "EXOPOLYPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "METAPHOSPHATASE"
---

# EXOPOLYPHOSPHATASE-RXN

`reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:EXOPOLYPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Long-Chain-Polyphosphate + WATER -> Long-Chain-Polyphosphate + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Long-Chain-Polyphosphate + WATER -> Long-Chain-Polyphosphate + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by exopolyphosphatase (complex.ecocyc.PPX-CPLX). Substrates: H2O (molecule.C00001), long chain polyphosphate (molecule.ecocyc.Long-Chain-Polyphosphate). Products: long chain polyphosphate (molecule.ecocyc.Long-Chain-Polyphosphate), phosphate (molecule.ecocyc.Pi).

## Annotation

Long-Chain-Polyphosphate + WATER -> Long-Chain-Polyphosphate + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.NH42SO4|molecule.ecocyc.NH42SO4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.PPX-CPLX|complex.ecocyc.PPX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Long-Chain-Polyphosphate|molecule.ecocyc.Long-Chain-Polyphosphate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Long-Chain-Polyphosphate|molecule.ecocyc.Long-Chain-Polyphosphate]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:EXOPOLYPHOSPHATASE-RXN`

## Notes

Long-Chain-Polyphosphate + WATER -> Long-Chain-Polyphosphate + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
