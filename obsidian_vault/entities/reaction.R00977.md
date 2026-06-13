---
entity_id: "reaction.R00977"
entity_type: "reaction"
name: "5,6-dihydrouracil:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00977"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00977"
---

# 5,6-dihydrouracil:NAD+ oxidoreductase

`reaction.R00977`

## Static

- Type: `reaction`
- Source: `KEGG:R00977`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5,6-Dihydrouracil + NAD+ Uracil + NADH + H+

## Biological Role

Catalyzed by preA (protein.P25889), preT (protein.P76440). Substrates: NAD+ (molecule.C00003), 5,6-Dihydrouracil (molecule.C00429). Products: NADH (molecule.C00004), H+ (molecule.C00080), Uracil (molecule.C00106).

## Annotation

5,6-Dihydrouracil + NAD+ <=> Uracil + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P25889|protein.P25889]] `KEGG` `database` - via EC:1.3.1.1
- `catalyzes` <-- [[protein.P76440|protein.P76440]] `KEGG` `database` - via EC:1.3.1.1
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00429 + C00003 <=> C00106 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00429 + C00003 <=> C00106 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `KEGG` `database` - C00429 + C00003 <=> C00106 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00429 + C00003 <=> C00106 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00429|molecule.C00429]] `KEGG` `database` - C00429 + C00003 <=> C00106 + C00004 + C00080

## External IDs

- `KEGG:R00977`

## Notes

EQUATION: C00429 + C00003 <=> C00106 + C00004 + C00080
