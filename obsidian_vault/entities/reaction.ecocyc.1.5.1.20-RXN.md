---
entity_id: "reaction.ecocyc.1.5.1.20-RXN"
entity_type: "reaction"
name: "1.5.1.20-RXN"
source_database: "EcoCyc"
source_id: "1.5.1.20-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "MTHFR"
---

# 1.5.1.20-RXN

`reaction.ecocyc.1.5.1.20-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.5.1.20-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-METHYL-THF-GLU-N + NAD-P-OR-NOP -> METHYLENE-THF-GLU-N + NADH-P-OR-NOP + PROTON; direction=REVERSIBLE EcoCyc reaction equation: 5-METHYL-THF-GLU-N + NAD-P-OR-NOP -> METHYLENE-THF-GLU-N + NADH-P-OR-NOP + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: a 5-methyltetrahydrofolate (molecule.ecocyc.5-METHYL-THF-GLU-N), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Annotation

5-METHYL-THF-GLU-N + NAD-P-OR-NOP -> METHYLENE-THF-GLU-N + NADH-P-OR-NOP + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.5-METHYL-THF-GLU-N|molecule.ecocyc.5-METHYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.5.1.20-RXN`

## Notes

5-METHYL-THF-GLU-N + NAD-P-OR-NOP -> METHYLENE-THF-GLU-N + NADH-P-OR-NOP + PROTON; direction=REVERSIBLE
