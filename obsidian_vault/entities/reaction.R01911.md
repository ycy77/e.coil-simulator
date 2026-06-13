---
entity_id: "reaction.R01911"
entity_type: "reaction"
name: "pyridoxine-5'-phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R01911"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01911"
---

# pyridoxine-5'-phosphate phosphohydrolase

`reaction.R01911`

## Static

- Type: `reaction`
- Source: `KEGG:R01911`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyridoxine + Orthophosphate Pyridoxine phosphate + H2O

## Biological Role

Catalyzed by ybhA (protein.P21829), yigL (protein.P27848). Substrates: Orthophosphate (molecule.C00009), Pyridoxine (molecule.C00314). Products: H2O (molecule.C00001), Pyridoxine phosphate (molecule.C00627).

## Annotation

Pyridoxine + Orthophosphate <=> Pyridoxine phosphate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21829|protein.P21829]] `KEGG` `database` - via EC:3.1.3.74
- `catalyzes` <-- [[protein.P27848|protein.P27848]] `KEGG` `database` - via EC:3.1.3.74
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00314 + C00009 <=> C00627 + C00001
- `is_product_of` <-- [[molecule.C00627|molecule.C00627]] `KEGG` `database` - C00314 + C00009 <=> C00627 + C00001
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00314 + C00009 <=> C00627 + C00001
- `is_substrate_of` <-- [[molecule.C00314|molecule.C00314]] `KEGG` `database` - C00314 + C00009 <=> C00627 + C00001

## External IDs

- `KEGG:R01911`

## Notes

EQUATION: C00314 + C00009 <=> C00627 + C00001
