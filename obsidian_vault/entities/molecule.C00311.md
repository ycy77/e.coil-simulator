---
entity_id: "molecule.C00311"
entity_type: "small_molecule"
name: "Isocitrate"
source_database: "KEGG"
source_id: "C00311"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Isocitrate"
  - "Isocitric acid"
  - "1-Hydroxytricarballylic acid"
  - "1-Hydroxypropane-1,2,3-tricarboxylic acid"
---

# Isocitrate

`molecule.C00311`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00311`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Isocitrate; Isocitric acid; 1-Hydroxytricarballylic acid; 1-Hydroxypropane-1,2,3-tricarboxylic acid

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Annotation

KEGG compound: Isocitrate; Isocitric acid; 1-Hydroxytricarballylic acid; 1-Hydroxypropane-1,2,3-tricarboxylic acid

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Outgoing Edges (7)

- `activates` --> [[reaction.ecocyc.DEPHOSICITDEHASE-RXN|reaction.ecocyc.DEPHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R01324|reaction.R01324]] `KEGG` `database` - C00158 <=> C00311
- `is_substrate_of` --> [[reaction.R00267|reaction.R00267]] `KEGG` `database` - C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00479|reaction.R00479]] `KEGG` `database` - C00311 <=> C00042 + C00048
- `is_substrate_of` --> [[reaction.R01899|reaction.R01899]] `KEGG` `database` - C00311 + C00006 <=> C05379 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R01900|reaction.R01900]] `KEGG` `database` - C00311 <=> C00417 + C00001
- `represses` --> [[reaction.ecocyc.PHOSICITDEHASE-RXN|reaction.ecocyc.PHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00311`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
