---
entity_id: "reaction.ecocyc.PYRUFLAVREDUCT-RXN"
entity_type: "reaction"
name: "PYRUFLAVREDUCT-RXN"
source_database: "EcoCyc"
source_id: "PYRUFLAVREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRUFLAVREDUCT-RXN

`reaction.ecocyc.PYRUFLAVREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRUFLAVREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is one avenue for conversion of pyruvate to acetyl-CoA and also functions as a pyruvate-dependent reduction of ferredoxin. EcoCyc reaction equation: PYRUVATE + CO-A + Oxidized-ferredoxins -> ACETYL-COA + CARBON-DIOXIDE + Reduced-ferredoxins + PROTON; direction=REVERSIBLE. This reaction is one avenue for conversion of pyruvate to acetyl-CoA and also functions as a pyruvate-dependent reduction of ferredoxin.

## Biological Role

Catalyzed by PYRUFLAVREDUCT-MONOMER (protein.ecocyc.PYRUFLAVREDUCT-MONOMER). Substrates: CoA (molecule.C00010), Pyruvate (molecule.C00022). Products: CO2 (molecule.C00011), Acetyl-CoA (molecule.C00024), H+ (molecule.C00080).

## Annotation

This reaction is one avenue for conversion of pyruvate to acetyl-CoA and also functions as a pyruvate-dependent reduction of ferredoxin.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.ecocyc.PYRUFLAVREDUCT-MONOMER|protein.ecocyc.PYRUFLAVREDUCT-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PYRUFLAVREDUCT-RXN`

## Notes

PYRUVATE + CO-A + Oxidized-ferredoxins -> ACETYL-COA + CARBON-DIOXIDE + Reduced-ferredoxins + PROTON; direction=REVERSIBLE
