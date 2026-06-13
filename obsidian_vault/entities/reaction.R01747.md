---
entity_id: "reaction.R01747"
entity_type: "reaction"
name: "(R)-glycerate:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R01747"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01747"
---

# (R)-glycerate:NADP+ oxidoreductase

`reaction.R01747`

## Static

- Type: `reaction`
- Source: `KEGG:R01747`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Glycerate + NADP+ 2-Hydroxy-3-oxopropanoate + NADPH + H+

## Biological Role

Catalyzed by garR (protein.P0ABQ2), glxR (protein.P77161). Substrates: NADP+ (molecule.C00006), D-Glycerate (molecule.C00258). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2-Hydroxy-3-oxopropanoate (molecule.C01146).

## Annotation

D-Glycerate + NADP+ <=> 2-Hydroxy-3-oxopropanoate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0ABQ2|protein.P0ABQ2]] `KEGG` `database` - via EC:1.1.1.60
- `catalyzes` <-- [[protein.P77161|protein.P77161]] `KEGG` `database` - via EC:1.1.1.60
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00258 + C00006 <=> C01146 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00258 + C00006 <=> C01146 + C00005 + C00080
- `is_product_of` <-- [[molecule.C01146|molecule.C01146]] `KEGG` `database` - C00258 + C00006 <=> C01146 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00258 + C00006 <=> C01146 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00258|molecule.C00258]] `KEGG` `database` - C00258 + C00006 <=> C01146 + C00005 + C00080

## External IDs

- `KEGG:R01747`

## Notes

EQUATION: C00258 + C00006 <=> C01146 + C00005 + C00080
