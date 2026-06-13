---
entity_id: "reaction.ecocyc.RXN-20155"
entity_type: "reaction"
name: "RXN-20155"
source_database: "EcoCyc"
source_id: "RXN-20155"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20155

`reaction.ecocyc.RXN-20155`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20155`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-S-Acetyl-Cysteines + ACETYL-COA -> ACETOACETYL-COA + PROT-CYS; direction=REVERSIBLE EcoCyc reaction equation: Protein-S-Acetyl-Cysteines + ACETYL-COA -> ACETOACETYL-COA + PROT-CYS; direction=REVERSIBLE.

## Biological Role

Substrates: Acetyl-CoA (molecule.C00024), a [protein] S-acetyl-L-cysteine (molecule.ecocyc.Protein-S-Acetyl-Cysteines). Products: Acetoacetyl-CoA (molecule.C00332), a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS).

## Annotation

Protein-S-Acetyl-Cysteines + ACETYL-COA -> ACETOACETYL-COA + PROT-CYS; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00332|molecule.C00332]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-S-Acetyl-Cysteines|molecule.ecocyc.Protein-S-Acetyl-Cysteines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20155`

## Notes

Protein-S-Acetyl-Cysteines + ACETYL-COA -> ACETOACETYL-COA + PROT-CYS; direction=REVERSIBLE
