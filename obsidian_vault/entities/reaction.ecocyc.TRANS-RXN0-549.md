---
entity_id: "reaction.ecocyc.TRANS-RXN0-549"
entity_type: "reaction"
name: "TRANS-RXN0-549"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-549"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-549

`reaction.ecocyc.TRANS-RXN0-549`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-549`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-1192 -> CPD0-1192; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1192 -> CPD0-1192; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by poly-N-acetyl-D-glucosamine synthase (complex.ecocyc.CPLX0-7994). Substrates: poly-β-1,6-N-acetyl-D-glucosamine (molecule.ecocyc.CPD0-1192). Products: poly-β-1,6-N-acetyl-D-glucosamine (molecule.ecocyc.CPD0-1192).

## Enriched Pathways

- `ecocyc.PWY0-1609` poly-β-1,6-N-acetyl-D-glucosamine biosynthesis (EcoCyc)

## Annotation

CPD0-1192 -> CPD0-1192; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1609` poly-β-1,6-N-acetyl-D-glucosamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7994|complex.ecocyc.CPLX0-7994]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1192|molecule.ecocyc.CPD0-1192]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1192|molecule.ecocyc.CPD0-1192]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-549`

## Notes

CPD0-1192 -> CPD0-1192; direction=PHYSIOL-LEFT-TO-RIGHT
