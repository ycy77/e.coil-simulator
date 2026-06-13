---
entity_id: "reaction.R01163"
entity_type: "reaction"
name: "L-histidinal:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R01163"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01163"
---

# L-histidinal:NAD+ oxidoreductase

`reaction.R01163`

## Static

- Type: `reaction`
- Source: `KEGG:R01163`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Histidinal + H2O + NAD+ L-Histidine + NADH + H+

## Biological Role

Catalyzed by hisD (protein.P06988). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), L-Histidinal (molecule.C01929). Products: NADH (molecule.C00004), H+ (molecule.C00080), L-Histidine (molecule.C00135).

## Annotation

L-Histidinal + H2O + NAD+ <=> L-Histidine + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P06988|protein.P06988]] `KEGG` `database` - via EC:1.1.1.23
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00135|molecule.C00135]] `KEGG` `database` - C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C01929|molecule.C01929]] `KEGG` `database` - C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080

## External IDs

- `KEGG:R01163`

## Notes

EQUATION: C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080
