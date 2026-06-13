---
entity_id: "reaction.R03431"
entity_type: "reaction"
name: "3-(3,5-diiodo-4-hydroxyphenyl)lactate:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R03431"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03431"
---

# 3-(3,5-diiodo-4-hydroxyphenyl)lactate:NAD+ oxidoreductase

`reaction.R03431`

## Static

- Type: `reaction`
- Source: `KEGG:R03431`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-(3,5-Diiodo-4-hydroxyphenyl)lactate + NAD+ 3,5-Diiodo-4-hydroxyphenylpyruvate + NADH + H+

## Biological Role

Catalyzed by mdh (protein.P61889). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Annotation

3-(3,5-Diiodo-4-hydroxyphenyl)lactate + NAD+ <=> 3,5-Diiodo-4-hydroxyphenylpyruvate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P61889|protein.P61889]] `KEGG` `database` - via EC:1.1.1.37
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C04367 + C00003 <=> C01244 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C04367 + C00003 <=> C01244 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C04367 + C00003 <=> C01244 + C00004 + C00080

## External IDs

- `KEGG:R03431`

## Notes

EQUATION: C04367 + C00003 <=> C01244 + C00004 + C00080
