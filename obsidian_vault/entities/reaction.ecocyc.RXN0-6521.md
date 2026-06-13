---
entity_id: "reaction.ecocyc.RXN0-6521"
entity_type: "reaction"
name: "RXN0-6521"
source_database: "EcoCyc"
source_id: "RXN0-6521"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6521

`reaction.ecocyc.RXN0-6521`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6521`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNASE-E-MRNA-PROCESSING-SUBSTRATE + WATER -> RNASE-E-PROCESSING-PRODUCT-MRNA + mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: RNASE-E-MRNA-PROCESSING-SUBSTRATE + WATER -> RNASE-E-PROCESSING-PRODUCT-MRNA + mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ribonuclease E (complex.ecocyc.CPLX0-3461). Substrates: H2O (molecule.C00001).

## Annotation

RNASE-E-MRNA-PROCESSING-SUBSTRATE + WATER -> RNASE-E-PROCESSING-PRODUCT-MRNA + mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3461|complex.ecocyc.CPLX0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6521`

## Notes

RNASE-E-MRNA-PROCESSING-SUBSTRATE + WATER -> RNASE-E-PROCESSING-PRODUCT-MRNA + mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT
