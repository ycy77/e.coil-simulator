---
entity_id: "reaction.R05838"
entity_type: "reaction"
name: "pyridoxine 5'-phosphate synthase"
source_database: "KEGG"
source_id: "R05838"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05838"
---

# pyridoxine 5'-phosphate synthase

`reaction.R05838`

## Static

- Type: `reaction`
- Source: `KEGG:R05838`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Amino-2-oxopropyl phosphate + 1-Deoxy-D-xylulose 5-phosphate Pyridoxine phosphate + Orthophosphate + 2 H2O

## Biological Role

Catalyzed by pdxJ (protein.P0A794). Substrates: 1-Deoxy-D-xylulose 5-phosphate (molecule.C11437), 3-Amino-2-oxopropyl phosphate (molecule.C11638). Products: H2O (molecule.C00001), Orthophosphate (molecule.C00009), Pyridoxine phosphate (molecule.C00627).

## Annotation

3-Amino-2-oxopropyl phosphate + 1-Deoxy-D-xylulose 5-phosphate <=> Pyridoxine phosphate + Orthophosphate + 2 H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A794|protein.P0A794]] `KEGG` `database` - via EC:2.6.99.2
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C11638 + C11437 <=> C00627 + C00009 + 2 C00001
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C11638 + C11437 <=> C00627 + C00009 + 2 C00001
- `is_product_of` <-- [[molecule.C00627|molecule.C00627]] `KEGG` `database` - C11638 + C11437 <=> C00627 + C00009 + 2 C00001
- `is_substrate_of` <-- [[molecule.C11437|molecule.C11437]] `KEGG` `database` - C11638 + C11437 <=> C00627 + C00009 + 2 C00001
- `is_substrate_of` <-- [[molecule.C11638|molecule.C11638]] `KEGG` `database` - C11638 + C11437 <=> C00627 + C00009 + 2 C00001

## External IDs

- `KEGG:R05838`

## Notes

EQUATION: C11638 + C11437 <=> C00627 + C00009 + 2 C00001
