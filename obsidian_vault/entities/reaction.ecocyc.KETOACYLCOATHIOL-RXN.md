---
entity_id: "reaction.ecocyc.KETOACYLCOATHIOL-RXN"
entity_type: "reaction"
name: "KETOACYLCOATHIOL-RXN"
source_database: "EcoCyc"
source_id: "KETOACYLCOATHIOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# KETOACYLCOATHIOL-RXN

`reaction.ecocyc.KETOACYLCOATHIOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KETOACYLCOATHIOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The final reaction in the β-oxidation cycle, releases product acetyl CoA and an acyl CoA fatty acid two carbons shorter, ready to go through β-oxidation reactions again. EcoCyc reaction equation: Saturated-Fatty-Acyl-CoA + ACETYL-COA -> 3-KETOACYL-COA + CO-A; direction=REVERSIBLE. The final reaction in the β-oxidation cycle, releases product acetyl CoA and an acyl CoA fatty acid two carbons shorter, ready to go through β-oxidation reactions again.

## Biological Role

Catalyzed by fadA (protein.P21151), fadI (protein.P76503). Substrates: Acetyl-CoA (molecule.C00024), a 2,3,4-saturated fatty acyl CoA (molecule.ecocyc.Saturated-Fatty-Acyl-CoA). Products: CoA (molecule.C00010), a 2,3,4-saturated 3-oxoacyl-CoA (molecule.ecocyc.3-KETOACYL-COA).

## Enriched Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Annotation

The final reaction in the β-oxidation cycle, releases product acetyl CoA and an acyl CoA fatty acid two carbons shorter, ready to go through β-oxidation reactions again.

## Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.3-KETOACYL-COA|molecule.ecocyc.3-KETOACYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Saturated-Fatty-Acyl-CoA|molecule.ecocyc.Saturated-Fatty-Acyl-CoA]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:KETOACYLCOATHIOL-RXN`

## Notes

Saturated-Fatty-Acyl-CoA + ACETYL-COA -> 3-KETOACYL-COA + CO-A; direction=REVERSIBLE
