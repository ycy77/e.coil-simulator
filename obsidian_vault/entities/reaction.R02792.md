---
entity_id: "reaction.R02792"
entity_type: "reaction"
name: "3alpha,7alpha,12alpha-trihydroxy-5beta-cholanate:NAD+ 7-oxidoreductase"
source_database: "KEGG"
source_id: "R02792"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02792"
---

# 3alpha,7alpha,12alpha-trihydroxy-5beta-cholanate:NAD+ 7-oxidoreductase

`reaction.R02792`

## Static

- Type: `reaction`
- Source: `KEGG:R02792`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cholic acid + NAD+ 7-Oxodeoxycholate + NADH + H+

## Biological Role

Catalyzed by hdhA (protein.P0AET8). Substrates: NAD+ (molecule.C00003), Cholic acid (molecule.C00695). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Annotation

Cholic acid + NAD+ <=> 7-Oxodeoxycholate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AET8|protein.P0AET8]] `KEGG` `database` - via EC:1.1.1.159
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00695 + C00003 <=> C04643 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00695 + C00003 <=> C04643 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00695 + C00003 <=> C04643 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00695|molecule.C00695]] `KEGG` `database` - C00695 + C00003 <=> C04643 + C00004 + C00080

## External IDs

- `KEGG:R02792`

## Notes

EQUATION: C00695 + C00003 <=> C04643 + C00004 + C00080
