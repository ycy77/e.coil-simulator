---
entity_id: "reaction.ecocyc.PYFLAVOXRE-RXN"
entity_type: "reaction"
name: "PYFLAVOXRE-RXN"
source_database: "EcoCyc"
source_id: "PYFLAVOXRE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYFLAVOXRE-RXN

`reaction.ecocyc.PYFLAVOXRE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYFLAVOXRE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PYRUVATE + CO-A + Oxidized-flavodoxins + PROTON -> ACETYL-COA + CARBON-DIOXIDE + Reduced-flavodoxins; direction=REVERSIBLE EcoCyc reaction equation: PYRUVATE + CO-A + Oxidized-flavodoxins + PROTON -> ACETYL-COA + CARBON-DIOXIDE + Reduced-flavodoxins; direction=REVERSIBLE.

## Biological Role

Catalyzed by ydbK (protein.P52647). Substrates: CoA (molecule.C00010), Pyruvate (molecule.C00022), H+ (molecule.C00080). Products: CO2 (molecule.C00011), Acetyl-CoA (molecule.C00024).

## Annotation

PYRUVATE + CO-A + Oxidized-flavodoxins + PROTON -> ACETYL-COA + CARBON-DIOXIDE + Reduced-flavodoxins; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P52647|protein.P52647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PYFLAVOXRE-RXN`

## Notes

PYRUVATE + CO-A + Oxidized-flavodoxins + PROTON -> ACETYL-COA + CARBON-DIOXIDE + Reduced-flavodoxins; direction=REVERSIBLE
