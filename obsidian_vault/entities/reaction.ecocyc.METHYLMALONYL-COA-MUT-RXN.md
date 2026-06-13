---
entity_id: "reaction.ecocyc.METHYLMALONYL-COA-MUT-RXN"
entity_type: "reaction"
name: "METHYLMALONYL-COA-MUT-RXN"
source_database: "EcoCyc"
source_id: "METHYLMALONYL-COA-MUT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# METHYLMALONYL-COA-MUT-RXN

`reaction.ecocyc.METHYLMALONYL-COA-MUT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METHYLMALONYL-COA-MUT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third reaction of the methylmalonyl pathway of propionate metabolism. EcoCyc reaction equation: METHYL-MALONYL-COA -> SUC-COA; direction=REVERSIBLE. This is the third reaction of the methylmalonyl pathway of propionate metabolism.

## Biological Role

Catalyzed by methylmalonyl-CoA mutase (complex.ecocyc.CPLX0-7741). Substrates: (R)-Methylmalonyl-CoA (molecule.C01213). Products: Succinyl-CoA (molecule.C00091).

## Enriched Pathways

- `ecocyc.PROPIONMET-PWY` propanoyl CoA degradation I (EcoCyc)
- `ecocyc.PWY0-43` conversion of succinate to propanoate (EcoCyc)

## Annotation

This is the third reaction of the methylmalonyl pathway of propionate metabolism.

## Pathways

- `ecocyc.PROPIONMET-PWY` propanoyl CoA degradation I (EcoCyc)
- `ecocyc.PWY0-43` conversion of succinate to propanoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7741|complex.ecocyc.CPLX0-7741]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01213|molecule.C01213]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:METHYLMALONYL-COA-MUT-RXN`

## Notes

METHYL-MALONYL-COA -> SUC-COA; direction=REVERSIBLE
