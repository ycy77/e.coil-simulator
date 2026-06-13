---
entity_id: "reaction.R11911"
entity_type: "reaction"
name: "L-carnitine,NADPH:oxygen oxidoreductase (trimethylamine-forming)"
source_database: "KEGG"
source_id: "R11911"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11911"
---

# L-carnitine,NADPH:oxygen oxidoreductase (trimethylamine-forming)

`reaction.R11911`

## Static

- Type: `reaction`
- Source: `KEGG:R11911`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Carnitine + NADPH + H+ + Oxygen (3R)-3-Hydroxy-4-oxobutanoate + Trimethylamine + NADP+ + H2O

## Biological Role

Catalyzed by yeaW (protein.P0ABR7), yeaX (protein.P76254). Substrates: NADPH (molecule.C00005), Oxygen (molecule.C00007), H+ (molecule.C00080). Products: H2O (molecule.C00001), NADP+ (molecule.C00006), Trimethylamine (molecule.C00565).

## Annotation

L-Carnitine + NADPH + H+ + Oxygen <=> (3R)-3-Hydroxy-4-oxobutanoate + Trimethylamine + NADP+ + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0ABR7|protein.P0ABR7]] `KEGG` `database` - via EC:1.14.13.239
- `catalyzes` <-- [[protein.P76254|protein.P76254]] `KEGG` `database` - via EC:1.14.13.239
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001
- `is_product_of` <-- [[molecule.C00565|molecule.C00565]] `KEGG` `database` - C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001

## External IDs

- `KEGG:R11911`

## Notes

EQUATION: C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001
