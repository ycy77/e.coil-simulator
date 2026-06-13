---
entity_id: "reaction.ecocyc.MEN-FE-RXN"
entity_type: "reaction"
name: "MEN-FE-RXN"
source_database: "EcoCyc"
source_id: "MEN-FE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MEN-FE-RXN

`reaction.ecocyc.MEN-FE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MEN-FE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + Ox-Menaquinone-8-Oxidoreductases + FeS-Proteins-Reduced -> PROTON + Red-Menaquinol-8-Oxidoreductases + FeS-Proteins; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + Ox-Menaquinone-8-Oxidoreductases + FeS-Proteins-Reduced -> PROTON + Red-Menaquinol-8-Oxidoreductases + FeS-Proteins; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080). Products: H+ (molecule.C00080).

## Annotation

PROTON + Ox-Menaquinone-8-Oxidoreductases + FeS-Proteins-Reduced -> PROTON + Red-Menaquinol-8-Oxidoreductases + FeS-Proteins; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MEN-FE-RXN`

## Notes

PROTON + Ox-Menaquinone-8-Oxidoreductases + FeS-Proteins-Reduced -> PROTON + Red-Menaquinol-8-Oxidoreductases + FeS-Proteins; direction=LEFT-TO-RIGHT
