---
entity_id: "reaction.ecocyc.RXN-20154"
entity_type: "reaction"
name: "RXN-20154"
source_database: "EcoCyc"
source_id: "RXN-20154"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20154

`reaction.ecocyc.RXN-20154`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20154`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYL-COA + PROT-CYS -> Protein-S-Acetyl-Cysteines + CO-A; direction=REVERSIBLE EcoCyc reaction equation: ACETYL-COA + PROT-CYS -> Protein-S-Acetyl-Cysteines + CO-A; direction=REVERSIBLE.

## Biological Role

Substrates: Acetyl-CoA (molecule.C00024), a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS). Products: CoA (molecule.C00010), a [protein] S-acetyl-L-cysteine (molecule.ecocyc.Protein-S-Acetyl-Cysteines).

## Annotation

ACETYL-COA + PROT-CYS -> Protein-S-Acetyl-Cysteines + CO-A; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-S-Acetyl-Cysteines|molecule.ecocyc.Protein-S-Acetyl-Cysteines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20154`

## Notes

ACETYL-COA + PROT-CYS -> Protein-S-Acetyl-Cysteines + CO-A; direction=REVERSIBLE
