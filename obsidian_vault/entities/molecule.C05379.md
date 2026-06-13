---
entity_id: "molecule.C05379"
entity_type: "small_molecule"
name: "Oxalosuccinate"
source_database: "KEGG"
source_id: "C05379"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Oxalosuccinate"
  - "Oxalosuccinic acid"
---

# Oxalosuccinate

`molecule.C05379`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05379`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Oxalosuccinate; Oxalosuccinic acid

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)

## Annotation

KEGG compound: Oxalosuccinate; Oxalosuccinic acid

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R01899|reaction.R01899]] `KEGG` `database` - C00311 + C00006 <=> C05379 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.RXN-9951|reaction.ecocyc.RXN-9951]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00268|reaction.R00268]] `KEGG` `database` - C05379 <=> C00026 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8642|reaction.ecocyc.RXN-8642]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05379`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
