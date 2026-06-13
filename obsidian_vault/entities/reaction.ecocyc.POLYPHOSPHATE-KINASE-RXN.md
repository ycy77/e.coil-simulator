---
entity_id: "reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN"
entity_type: "reaction"
name: "POLYPHOSPHATE-KINASE-RXN"
source_database: "EcoCyc"
source_id: "POLYPHOSPHATE-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# POLYPHOSPHATE-KINASE-RXN

`reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:POLYPHOSPHATE-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Long-Chain-Polyphosphate -> ADP + Long-Chain-Polyphosphate; direction=REVERSIBLE EcoCyc reaction equation: ATP + Long-Chain-Polyphosphate -> ADP + Long-Chain-Polyphosphate; direction=REVERSIBLE.

## Biological Role

Catalyzed by polyphosphate kinase (complex.ecocyc.PPK-CPLX). Substrates: ATP (molecule.C00002), long chain polyphosphate (molecule.ecocyc.Long-Chain-Polyphosphate). Products: ADP (molecule.C00008), long chain polyphosphate (molecule.ecocyc.Long-Chain-Polyphosphate).

## Annotation

ATP + Long-Chain-Polyphosphate -> ADP + Long-Chain-Polyphosphate; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `activates` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-1470|molecule.ecocyc.CPD0-1470]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.PPK-CPLX|complex.ecocyc.PPK-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Long-Chain-Polyphosphate|molecule.ecocyc.Long-Chain-Polyphosphate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Long-Chain-Polyphosphate|molecule.ecocyc.Long-Chain-Polyphosphate]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1470|molecule.ecocyc.CPD0-1470]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.KCL|molecule.ecocyc.KCL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.NH42SO4|molecule.ecocyc.NH42SO4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:POLYPHOSPHATE-KINASE-RXN`

## Notes

ATP + Long-Chain-Polyphosphate -> ADP + Long-Chain-Polyphosphate; direction=REVERSIBLE
