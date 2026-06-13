---
entity_id: "reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN"
entity_type: "reaction"
name: "ACETYL-COA-ACETYLTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "ACETYL-COA-ACETYLTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETYL-COA-ACETYLTRANSFER-RXN

`reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETYL-COA-ACETYLTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The second step in the degradation of short-chain fatty acid acetoacetate. EcoCyc reaction equation: ACETYL-COA -> ACETOACETYL-COA + CO-A; direction=REVERSIBLE. The second step in the degradation of short-chain fatty acid acetoacetate.

## Biological Role

Catalyzed by acetyl-CoA acetyltransferase (complex.ecocyc.ACETYL-COA-ACETYLTRANSFER-CPLX). Substrates: Acetyl-CoA (molecule.C00024). Products: CoA (molecule.C00010), Acetoacetyl-CoA (molecule.C00332).

## Enriched Pathways

- `ecocyc.ACETOACETATE-DEG-PWY` acetoacetate degradation (to acetyl CoA) (EcoCyc)
- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

The second step in the degradation of short-chain fatty acid acetoacetate.

## Pathways

- `ecocyc.ACETOACETATE-DEG-PWY` acetoacetate degradation (to acetyl CoA) (EcoCyc)
- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ACETYL-COA-ACETYLTRANSFER-CPLX|complex.ecocyc.ACETYL-COA-ACETYLTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00332|molecule.C00332]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00332|molecule.C00332]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETYL-COA-ACETYLTRANSFER-RXN`

## Notes

ACETYL-COA -> ACETOACETYL-COA + CO-A; direction=REVERSIBLE
