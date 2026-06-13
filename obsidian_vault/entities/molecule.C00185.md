---
entity_id: "molecule.C00185"
entity_type: "small_molecule"
name: "Cellobiose"
source_database: "KEGG"
source_id: "C00185"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cellobiose"
  - "1-beta-D-Glucopyranosyl-4-D-glucopyranose"
---

# Cellobiose

`molecule.C00185`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00185`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cellobiose; 1-beta-D-Glucopyranosyl-4-D-glucopyranose EcoCyc common name: D-cellobiose.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Cellobiose; 1-beta-D-Glucopyranosyl-4-D-glucopyranose

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R02887|reaction.R02887]] `KEGG` `database` - C01898 + (n-2) C00001 <=> (n-2) C00031 + C00185
- `is_substrate_of` --> [[reaction.R00026|reaction.R00026]] `KEGG` `database` - C00185 + C00001 <=> 2 C00221
- `is_substrate_of` --> [[reaction.R00306|reaction.R00306]] `KEGG` `database` - C00185 + C00001 <=> 2 C00031

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00185`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
