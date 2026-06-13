---
entity_id: "reaction.ecocyc.ACETATE--COA-LIGASE-RXN"
entity_type: "reaction"
name: "ACETATE--COA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "ACETATE--COA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETATE--COA-LIGASE-RXN

`reaction.ecocyc.ACETATE--COA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETATE--COA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CO-A + ACET + ATP -> ACETYL-COA + PPI + AMP; direction=REVERSIBLE EcoCyc reaction equation: CO-A + ACET + ATP -> ACETYL-COA + PPI + AMP; direction=REVERSIBLE.

## Biological Role

Catalyzed by acs (protein.P27550). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Acetate (molecule.C00033). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), Acetyl-CoA (molecule.C00024).

## Enriched Pathways

- `ecocyc.PWY0-1313` acetate conversion to acetyl-CoA (EcoCyc)

## Annotation

CO-A + ACET + ATP -> ACETYL-COA + PPI + AMP; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1313` acetate conversion to acetyl-CoA (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P27550|protein.P27550]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00163|molecule.C00163]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETATE--COA-LIGASE-RXN`

## Notes

CO-A + ACET + ATP -> ACETYL-COA + PPI + AMP; direction=REVERSIBLE
