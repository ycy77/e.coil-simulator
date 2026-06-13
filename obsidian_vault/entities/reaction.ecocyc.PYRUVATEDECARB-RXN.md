---
entity_id: "reaction.ecocyc.PYRUVATEDECARB-RXN"
entity_type: "reaction"
name: "PYRUVATEDECARB-RXN"
source_database: "EcoCyc"
source_id: "PYRUVATEDECARB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRUVATEDECARB-RXN

`reaction.ecocyc.PYRUVATEDECARB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRUVATEDECARB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Note: Lipoamide is used to substitute for lipoate in assays conducted in vitro. EcoCyc reaction equation: PROTON + PYRUVATE + LIPOAMIDE -> S-ACETYLDIHYDROLIPOAMIDE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. Note: Lipoamide is used to substitute for lipoate in assays conducted in vitro.

## Biological Role

Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080), Lipoylprotein (molecule.C02051). Products: CO2 (molecule.C00011), S-acetyldihydrolipoamide (molecule.ecocyc.S-ACETYLDIHYDROLIPOAMIDE).

## Annotation

Note: Lipoamide is used to substitute for lipoate in assays conducted in vitro.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.S-ACETYLDIHYDROLIPOAMIDE|molecule.ecocyc.S-ACETYLDIHYDROLIPOAMIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02051|molecule.C02051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PYRUVATEDECARB-RXN`

## Notes

PROTON + PYRUVATE + LIPOAMIDE -> S-ACETYLDIHYDROLIPOAMIDE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
