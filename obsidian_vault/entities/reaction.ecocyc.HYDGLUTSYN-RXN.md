---
entity_id: "reaction.ecocyc.HYDGLUTSYN-RXN"
entity_type: "reaction"
name: "HYDGLUTSYN-RXN"
source_database: "EcoCyc"
source_id: "HYDGLUTSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HYDGLUTSYN-RXN

`reaction.ecocyc.HYDGLUTSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HYDGLUTSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of a pathway that allows the formation of C4 acids directly from propionate. EcoCyc reaction equation: PROPIONYL-COA + WATER + GLYOX -> 2-HYDROXYGLUTARIC_ACID + PROTON + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of a pathway that allows the formation of C4 acids directly from propionate.

## Biological Role

Catalyzed by HYDGLUTSYN-MONOMER (protein.ecocyc.HYDGLUTSYN-MONOMER). Substrates: H2O (molecule.C00001), Glyoxylate (molecule.C00048), Propanoyl-CoA (molecule.C00100). Products: CoA (molecule.C00010), H+ (molecule.C00080), 2-Hydroxyglutarate (molecule.C02630).

## Annotation

This reaction is part of a pathway that allows the formation of C4 acids directly from propionate.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.ecocyc.HYDGLUTSYN-MONOMER|protein.ecocyc.HYDGLUTSYN-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02630|molecule.C02630]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HYDGLUTSYN-RXN`

## Notes

PROPIONYL-COA + WATER + GLYOX -> 2-HYDROXYGLUTARIC_ACID + PROTON + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
