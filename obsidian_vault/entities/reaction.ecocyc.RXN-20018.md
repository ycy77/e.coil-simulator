---
entity_id: "reaction.ecocyc.RXN-20018"
entity_type: "reaction"
name: "RXN-20018"
source_database: "EcoCyc"
source_id: "RXN-20018"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20018

`reaction.ecocyc.RXN-20018`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20018`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

a-reduced-DsbG-protein + PROTEIN-S-HYDROXY-CYSTEINE -> an-oxidized-DsbG-protein + PROT-CYS + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-reduced-DsbG-protein + PROTEIN-S-HYDROXY-CYSTEINE -> an-oxidized-DsbG-protein + PROT-CYS + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: a [protein]-S-hydroxy-L-cysteine (molecule.ecocyc.PROTEIN-S-HYDROXY-CYSTEINE). Products: H2O (molecule.C00001), a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS).

## Annotation

a-reduced-DsbG-protein + PROTEIN-S-HYDROXY-CYSTEINE -> an-oxidized-DsbG-protein + PROT-CYS + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.PROTEIN-S-HYDROXY-CYSTEINE|molecule.ecocyc.PROTEIN-S-HYDROXY-CYSTEINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20018`

## Notes

a-reduced-DsbG-protein + PROTEIN-S-HYDROXY-CYSTEINE -> an-oxidized-DsbG-protein + PROT-CYS + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
