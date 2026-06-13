---
entity_id: "reaction.ecocyc.3.5.2.17-RXN"
entity_type: "reaction"
name: "3.5.2.17-RXN"
source_database: "EcoCyc"
source_id: "3.5.2.17-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.5.2.17-RXN

`reaction.ecocyc.3.5.2.17-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.5.2.17-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

5-HYDROXYISOURATE + WATER -> PROTON + CPD-5821; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 5-HYDROXYISOURATE + WATER -> PROTON + CPD-5821; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hydroxyisourate hydrolase / transthyretin-related protein (complex.ecocyc.CPLX0-3961). Substrates: H2O (molecule.C00001), 5-Hydroxyisourate (molecule.C11821). Products: H+ (molecule.C00080), 5-Hydroxy-2-oxo-4-ureido-2,5-dihydro-1H-imidazole-5-carboxylate (molecule.C12248).

## Annotation

5-HYDROXYISOURATE + WATER -> PROTON + CPD-5821; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3961|complex.ecocyc.CPLX0-3961]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C12248|molecule.C12248]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11821|molecule.C11821]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.5.2.17-RXN`

## Notes

5-HYDROXYISOURATE + WATER -> PROTON + CPD-5821; direction=PHYSIOL-LEFT-TO-RIGHT
