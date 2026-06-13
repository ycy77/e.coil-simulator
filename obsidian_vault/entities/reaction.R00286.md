---
entity_id: "reaction.R00286"
entity_type: "reaction"
name: "UDP-glucose:NAD+ 6-oxidoreductase"
source_database: "KEGG"
source_id: "R00286"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00286"
---

# UDP-glucose:NAD+ 6-oxidoreductase

`reaction.R00286`

## Static

- Type: `reaction`
- Source: `KEGG:R00286`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-glucose + H2O + 2 NAD+ UDP-glucuronate + 2 NADH + 2 H+

## Biological Role

Catalyzed by ugd (protein.P76373). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), UDP-glucose (molecule.C00029). Products: NADH (molecule.C00004), H+ (molecule.C00080), UDP-glucuronate (molecule.C00167).

## Annotation

UDP-glucose + H2O + 2 NAD+ <=> UDP-glucuronate + 2 NADH + 2 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P76373|protein.P76373]] `KEGG` `database` - via EC:1.1.1.22
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080
- `is_product_of` <-- [[molecule.C00167|molecule.C00167]] `KEGG` `database` - C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `KEGG` `database` - C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080

## External IDs

- `KEGG:R00286`

## Notes

EQUATION: C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080
