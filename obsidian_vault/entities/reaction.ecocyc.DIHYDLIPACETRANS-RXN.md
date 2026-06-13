---
entity_id: "reaction.ecocyc.DIHYDLIPACETRANS-RXN"
entity_type: "reaction"
name: "DIHYDLIPACETRANS-RXN"
source_database: "EcoCyc"
source_id: "DIHYDLIPACETRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIHYDLIPACETRANS-RXN

`reaction.ecocyc.DIHYDLIPACETRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDLIPACETRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Note: Dihydrolipoamide is used to substitute for dihydrolipoate in assays conducted in vitro, and S-acetyldihydrolipoamide is used to substitute for S-acetyldihydrolipoate in vitro. EcoCyc reaction equation: ACETYL-COA + DIHYDROLIPOAMIDE -> CO-A + S-ACETYLDIHYDROLIPOAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT. Note: Dihydrolipoamide is used to substitute for dihydrolipoate in assays conducted in vitro, and S-acetyldihydrolipoamide is used to substitute for S-acetyldihydrolipoate in vitro.

## Biological Role

Substrates: Acetyl-CoA (molecule.C00024), Dihydrolipoylprotein (molecule.C02972). Products: CoA (molecule.C00010), S-acetyldihydrolipoamide (molecule.ecocyc.S-ACETYLDIHYDROLIPOAMIDE).

## Annotation

Note: Dihydrolipoamide is used to substitute for dihydrolipoate in assays conducted in vitro, and S-acetyldihydrolipoamide is used to substitute for S-acetyldihydrolipoate in vitro.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.S-ACETYLDIHYDROLIPOAMIDE|molecule.ecocyc.S-ACETYLDIHYDROLIPOAMIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02972|molecule.C02972]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DIHYDLIPACETRANS-RXN`

## Notes

ACETYL-COA + DIHYDROLIPOAMIDE -> CO-A + S-ACETYLDIHYDROLIPOAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT
