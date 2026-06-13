---
entity_id: "reaction.ecocyc.RXN-18434"
entity_type: "reaction"
name: "RXN-18434"
source_database: "EcoCyc"
source_id: "RXN-18434"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18434

`reaction.ecocyc.RXN-18434`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18434`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S5-N-terminal-L-alanine + ACETYL-COA -> Acetylated-S5-N-terminal-L-alanine + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S5-N-terminal-L-alanine + ACETYL-COA -> Acetylated-S5-N-terminal-L-alanine + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rimJ (protein.P0A948). Substrates: Acetyl-CoA (molecule.C00024), an N-terminal L-alanyl-[uS5 protein of 30S ribosome] (molecule.ecocyc.S5-N-terminal-L-alanine). Products: CoA (molecule.C00010), H+ (molecule.C00080), an N-terminal N-acetyl-L-alanyl-[uS5 protein of 30S ribosome] (molecule.ecocyc.Acetylated-S5-N-terminal-L-alanine).

## Annotation

S5-N-terminal-L-alanine + ACETYL-COA -> Acetylated-S5-N-terminal-L-alanine + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A948|protein.P0A948]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Acetylated-S5-N-terminal-L-alanine|molecule.ecocyc.Acetylated-S5-N-terminal-L-alanine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.S5-N-terminal-L-alanine|molecule.ecocyc.S5-N-terminal-L-alanine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18434`

## Notes

S5-N-terminal-L-alanine + ACETYL-COA -> Acetylated-S5-N-terminal-L-alanine + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
