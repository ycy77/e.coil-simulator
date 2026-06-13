---
entity_id: "reaction.R01745"
entity_type: "reaction"
name: "(R)-glycerate:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R01745"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01745"
---

# (R)-glycerate:NAD+ oxidoreductase

`reaction.R01745`

## Static

- Type: `reaction`
- Source: `KEGG:R01745`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Glycerate + NAD+ 2-Hydroxy-3-oxopropanoate + NADH + H+

## Biological Role

Catalyzed by garR (protein.P0ABQ2), glxR (protein.P77161). Substrates: NAD+ (molecule.C00003), D-Glycerate (molecule.C00258). Products: NADH (molecule.C00004), H+ (molecule.C00080), 2-Hydroxy-3-oxopropanoate (molecule.C01146).

## Annotation

D-Glycerate + NAD+ <=> 2-Hydroxy-3-oxopropanoate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0ABQ2|protein.P0ABQ2]] `KEGG` `database` - via EC:1.1.1.60
- `catalyzes` <-- [[protein.P77161|protein.P77161]] `KEGG` `database` - via EC:1.1.1.60
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00258 + C00003 <=> C01146 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00258 + C00003 <=> C01146 + C00004 + C00080
- `is_product_of` <-- [[molecule.C01146|molecule.C01146]] `KEGG` `database` - C00258 + C00003 <=> C01146 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00258 + C00003 <=> C01146 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00258|molecule.C00258]] `KEGG` `database` - C00258 + C00003 <=> C01146 + C00004 + C00080

## External IDs

- `KEGG:R01745`

## Notes

EQUATION: C00258 + C00003 <=> C01146 + C00004 + C00080
