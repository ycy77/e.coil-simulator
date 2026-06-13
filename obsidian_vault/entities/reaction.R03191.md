---
entity_id: "reaction.R03191"
entity_type: "reaction"
name: "UDP-N-acetylmuramate:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R03191"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03191"
---

# UDP-N-acetylmuramate:NADP+ oxidoreductase

`reaction.R03191`

## Static

- Type: `reaction`
- Source: `KEGG:R03191`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-acetylmuramate + NAD+ UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine + NADH + H+

## Biological Role

Catalyzed by murB (protein.P08373). Substrates: NAD+ (molecule.C00003), UDP-N-acetylmuramate (molecule.C01050). Products: NADH (molecule.C00004), H+ (molecule.C00080), UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine (molecule.C04631).

## Annotation

UDP-N-acetylmuramate + NAD+ <=> UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P08373|protein.P08373]] `KEGG` `database` - via EC:1.3.1.98
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C01050 + C00003 <=> C04631 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01050 + C00003 <=> C04631 + C00004 + C00080
- `is_product_of` <-- [[molecule.C04631|molecule.C04631]] `KEGG` `database` - C01050 + C00003 <=> C04631 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C01050 + C00003 <=> C04631 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C01050|molecule.C01050]] `KEGG` `database` - C01050 + C00003 <=> C04631 + C00004 + C00080

## External IDs

- `KEGG:R03191`

## Notes

EQUATION: C01050 + C00003 <=> C04631 + C00004 + C00080
