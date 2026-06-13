---
entity_id: "reaction.ecocyc.RXN-11662"
entity_type: "reaction"
name: "RXN-11662"
source_database: "EcoCyc"
source_id: "RXN-11662"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11662

`reaction.ecocyc.RXN-11662`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11662`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-3-HYDROXYBUTANOYL-COA + NAD -> ACETOACETYL-COA + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: S-3-HYDROXYBUTANOYL-COA + NAD -> ACETOACETYL-COA + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: NAD+ (molecule.C00003), (S)-3-Hydroxybutanoyl-CoA (molecule.C01144). Products: NADH (molecule.C00004), H+ (molecule.C00080), Acetoacetyl-CoA (molecule.C00332).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

S-3-HYDROXYBUTANOYL-COA + NAD -> ACETOACETYL-COA + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00332|molecule.C00332]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01144|molecule.C01144]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11662`

## Notes

S-3-HYDROXYBUTANOYL-COA + NAD -> ACETOACETYL-COA + NADH + PROTON; direction=REVERSIBLE
