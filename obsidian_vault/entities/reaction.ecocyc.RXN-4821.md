---
entity_id: "reaction.ecocyc.RXN-4821"
entity_type: "reaction"
name: "RXN-4821"
source_database: "EcoCyc"
source_id: "RXN-4821"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-4821

`reaction.ecocyc.RXN-4821`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-4821`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + WATER -> L-ALPHA-AMINO-EPSILON-KETO-PIMELATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + WATER -> L-ALPHA-AMINO-EPSILON-KETO-PIMELATE; direction=REVERSIBLE.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), 2,3,4,5-Tetrahydrodipicolinate (molecule.C03972). Products: L-2-Amino-6-oxoheptanedioate (molecule.C03871).

## Annotation

PROTON + DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + WATER -> L-ALPHA-AMINO-EPSILON-KETO-PIMELATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C03871|molecule.C03871]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03972|molecule.C03972]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-4821`

## Notes

PROTON + DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + WATER -> L-ALPHA-AMINO-EPSILON-KETO-PIMELATE; direction=REVERSIBLE
