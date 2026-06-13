---
entity_id: "reaction.ecocyc.DCUS-RXN"
entity_type: "reaction"
name: "DCUS-RXN"
source_database: "EcoCyc"
source_id: "DCUS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DCUS-RXN

`reaction.ecocyc.DCUS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DCUS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + CPLX0-8307 -> PHOSPHO-DCUS-MONOMER + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPLX0-8307 -> PHOSPHO-DCUS-MONOMER + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1468` DcuSR Two-Component Signal Transduction System, C4-dicarboxylate-dependent (EcoCyc)

## Annotation

ATP + CPLX0-8307 -> PHOSPHO-DCUS-MONOMER + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1468` DcuSR Two-Component Signal Transduction System, C4-dicarboxylate-dependent (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `activates` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DCUS-RXN`

## Notes

ATP + CPLX0-8307 -> PHOSPHO-DCUS-MONOMER + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
