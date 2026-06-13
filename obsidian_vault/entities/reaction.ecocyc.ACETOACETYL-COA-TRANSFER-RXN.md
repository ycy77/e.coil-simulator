---
entity_id: "reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN"
entity_type: "reaction"
name: "ACETOACETYL-COA-TRANSFER-RXN"
source_database: "EcoCyc"
source_id: "ACETOACETYL-COA-TRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETOACETYL-COA-TRANSFER-RXN

`reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETOACETYL-COA-TRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first step in the degradation of short-chain fatty acid acetoacetate. EcoCyc reaction equation: 3-KETOBUTYRATE + ACETYL-COA -> ACETOACETYL-COA + ACET; direction=REVERSIBLE. The first step in the degradation of short-chain fatty acid acetoacetate.

## Biological Role

Catalyzed by acetoacetyl-CoA transferase (complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX), ydiF (protein.P37766). Substrates: Acetyl-CoA (molecule.C00024), Acetoacetate (molecule.C00164). Products: Acetate (molecule.C00033), Acetoacetyl-CoA (molecule.C00332).

## Enriched Pathways

- `ecocyc.ACETOACETATE-DEG-PWY` acetoacetate degradation (to acetyl CoA) (EcoCyc)

## Annotation

The first step in the degradation of short-chain fatty acid acetoacetate.

## Pathways

- `ecocyc.ACETOACETATE-DEG-PWY` acetoacetate degradation (to acetyl CoA) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX|complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37766|protein.P37766]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00332|molecule.C00332]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00164|molecule.C00164]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETOACETYL-COA-TRANSFER-RXN`

## Notes

3-KETOBUTYRATE + ACETYL-COA -> ACETOACETYL-COA + ACET; direction=REVERSIBLE
