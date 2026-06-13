---
entity_id: "molecule.C00219"
entity_type: "small_molecule"
name: "Arachidonate"
source_database: "KEGG"
source_id: "C00219"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Arachidonate"
  - "Arachidonic acid"
  - "(5Z,8Z,11Z,14Z)-Icosatetraenoic acid"
  - "cis-5,8,11,14-Eicosatetraenoic acid"
  - "5Z,8Z,11Z,14Z-Eicosatetraenoic acid"
  - "(5Z,8Z,11Z,14Z)-Icosa-5,8,11,14-tetraenoic acid"
---

# Arachidonate

`molecule.C00219`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00219`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Arachidonate; Arachidonic acid; (5Z,8Z,11Z,14Z)-Icosatetraenoic acid; cis-5,8,11,14-Eicosatetraenoic acid; 5Z,8Z,11Z,14Z-Eicosatetraenoic acid; (5Z,8Z,11Z,14Z)-Icosa-5,8,11,14-tetraenoic acid

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

KEGG compound: Arachidonate; Arachidonic acid; (5Z,8Z,11Z,14Z)-Icosatetraenoic acid; cis-5,8,11,14-Eicosatetraenoic acid; 5Z,8Z,11Z,14Z-Eicosatetraenoic acid; (5Z,8Z,11Z,14Z)-Icosa-5,8,11,14-tetraenoic acid

## Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R01317|reaction.R01317]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00219
- `is_product_of` --> [[reaction.R08183|reaction.R08183]] `KEGG` `database` - C02249 + C00001 <=> C00010 + C00219

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00219`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
