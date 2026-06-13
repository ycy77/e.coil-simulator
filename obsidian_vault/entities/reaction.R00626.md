---
entity_id: "reaction.R00626"
entity_type: "reaction"
name: "phosphate-monoester phosphohydrolase"
source_database: "KEGG"
source_id: "R00626"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00626"
---

# phosphate-monoester phosphohydrolase

`reaction.R00626`

## Static

- Type: `reaction`
- Source: `KEGG:R00626`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Orthophosphoric monoester + H2O Alcohol + Orthophosphate

## Biological Role

Catalyzed by phoA (protein.P00634), appA (protein.P07102), aphA (protein.P0AE22). Substrates: H2O (molecule.C00001), Orthophosphoric monoester (molecule.C01153). Products: Orthophosphate (molecule.C00009).

## Annotation

Orthophosphoric monoester + H2O <=> Alcohol + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00634|protein.P00634]] `KEGG` `database` - via EC:3.1.3.1
- `catalyzes` <-- [[protein.P07102|protein.P07102]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` <-- [[protein.P0AE22|protein.P0AE22]] `KEGG` `database` - via EC:3.1.3.2
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C01153 + C00001 <=> C00069 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01153 + C00001 <=> C00069 + C00009
- `is_substrate_of` <-- [[molecule.C01153|molecule.C01153]] `KEGG` `database` - C01153 + C00001 <=> C00069 + C00009

## External IDs

- `KEGG:R00626`

## Notes

EQUATION: C01153 + C00001 <=> C00069 + C00009
