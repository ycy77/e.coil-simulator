---
entity_id: "reaction.R01158"
entity_type: "reaction"
name: "L-histidinol:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R01158"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01158"
---

# L-histidinol:NAD+ oxidoreductase

`reaction.R01158`

## Static

- Type: `reaction`
- Source: `KEGG:R01158`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Histidinol + 2 NAD+ + H2O L-Histidine + 2 NADH + 2 H+

## Biological Role

Catalyzed by hisD (protein.P06988). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), L-Histidinol (molecule.C00860). Products: NADH (molecule.C00004), H+ (molecule.C00080), L-Histidine (molecule.C00135).

## Annotation

L-Histidinol + 2 NAD+ + H2O <=> L-Histidine + 2 NADH + 2 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P06988|protein.P06988]] `KEGG` `database` - via EC:1.1.1.23
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080
- `is_product_of` <-- [[molecule.C00135|molecule.C00135]] `KEGG` `database` - C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00860|molecule.C00860]] `KEGG` `database` - C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080

## External IDs

- `KEGG:R01158`

## Notes

EQUATION: C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080
