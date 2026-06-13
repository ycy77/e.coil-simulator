---
entity_id: "reaction.ecocyc.RXN0-7440"
entity_type: "reaction"
name: "RXN0-7440"
source_database: "EcoCyc"
source_id: "RXN0-7440"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7440

`reaction.ecocyc.RXN0-7440`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7440`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-SELENOCYSTEINE + Selenocysteine-Lyase-L-Cysteine -> Selenocysteine-Lyase-S-selanyl-L-Cysteine + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-SELENOCYSTEINE + Selenocysteine-Lyase-L-Cysteine -> Selenocysteine-Lyase-S-selanyl-L-Cysteine + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Selenocysteine (molecule.C05688), a [selenocysteine lyase]-L-cysteine (molecule.ecocyc.Selenocysteine-Lyase-L-Cysteine). Products: L-Alanine (molecule.C00041), a [selenocysteine lyase]-S-selenopersulfide (molecule.ecocyc.Selenocysteine-Lyase-S-selanyl-L-Cysteine).

## Annotation

L-SELENOCYSTEINE + Selenocysteine-Lyase-L-Cysteine -> Selenocysteine-Lyase-S-selanyl-L-Cysteine + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Selenocysteine-Lyase-S-selanyl-L-Cysteine|molecule.ecocyc.Selenocysteine-Lyase-S-selanyl-L-Cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05688|molecule.C05688]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Selenocysteine-Lyase-L-Cysteine|molecule.ecocyc.Selenocysteine-Lyase-L-Cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7440`

## Notes

L-SELENOCYSTEINE + Selenocysteine-Lyase-L-Cysteine -> Selenocysteine-Lyase-S-selanyl-L-Cysteine + L-ALPHA-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
