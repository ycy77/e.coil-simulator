---
entity_id: "reaction.R03192"
entity_type: "reaction"
name: "UDP-N-acetylmuramate:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R03192"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03192"
---

# UDP-N-acetylmuramate:NADP+ oxidoreductase

`reaction.R03192`

## Static

- Type: `reaction`
- Source: `KEGG:R03192`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-acetylmuramate + NADP+ UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine + NADPH + H+

## Biological Role

Catalyzed by murB (protein.P08373). Substrates: NADP+ (molecule.C00006), UDP-N-acetylmuramate (molecule.C01050). Products: NADPH (molecule.C00005), H+ (molecule.C00080), UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine (molecule.C04631).

## Annotation

UDP-N-acetylmuramate + NADP+ <=> UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P08373|protein.P08373]] `KEGG` `database` - via EC:1.3.1.98
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C01050 + C00006 <=> C04631 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01050 + C00006 <=> C04631 + C00005 + C00080
- `is_product_of` <-- [[molecule.C04631|molecule.C04631]] `KEGG` `database` - C01050 + C00006 <=> C04631 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C01050 + C00006 <=> C04631 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C01050|molecule.C01050]] `KEGG` `database` - C01050 + C00006 <=> C04631 + C00005 + C00080

## External IDs

- `KEGG:R03192`

## Notes

EQUATION: C01050 + C00006 <=> C04631 + C00005 + C00080
