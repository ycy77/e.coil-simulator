---
entity_id: "molecule.C02249"
entity_type: "small_molecule"
name: "Arachidonyl-CoA"
source_database: "KEGG"
source_id: "C02249"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Arachidonyl-CoA"
  - "Arachidonoyl-CoA"
  - "(5Z,8Z,11Z,14Z)-Icosatetraenoyl-CoA"
---

# Arachidonyl-CoA

`molecule.C02249`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02249`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Arachidonyl-CoA; Arachidonoyl-CoA; (5Z,8Z,11Z,14Z)-Icosatetraenoyl-CoA

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

KEGG compound: Arachidonyl-CoA; Arachidonoyl-CoA; (5Z,8Z,11Z,14Z)-Icosatetraenoyl-CoA

## Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Outgoing Edges (1)

- `is_substrate_of` --> [[reaction.R08183|reaction.R08183]] `KEGG` `database` - C02249 + C00001 <=> C00010 + C00219

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02249`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
