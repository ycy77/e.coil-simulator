---
entity_id: "reaction.R04439"
entity_type: "reaction"
name: "(R)-2,3-dihydroxy-3-methylbutanoate:NADP+ oxidoreductase (isomerizing)"
source_database: "KEGG"
source_id: "R04439"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04439"
---

# (R)-2,3-dihydroxy-3-methylbutanoate:NADP+ oxidoreductase (isomerizing)

`reaction.R04439`

## Static

- Type: `reaction`
- Source: `KEGG:R04439`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(R)-2,3-Dihydroxy-3-methylbutanoate + NADP+ (S)-2-Acetolactate + NADPH + H+

## Biological Role

Catalyzed by ilvC (protein.P05793). Substrates: NADP+ (molecule.C00006), (R)-2,3-Dihydroxy-3-methylbutanoate (molecule.C04272). Products: NADPH (molecule.C00005), H+ (molecule.C00080), (S)-2-Acetolactate (molecule.C06010).

## Annotation

(R)-2,3-Dihydroxy-3-methylbutanoate + NADP+ <=> (S)-2-Acetolactate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P05793|protein.P05793]] `KEGG` `database` - via EC:1.1.1.86
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C04272 + C00006 <=> C06010 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C04272 + C00006 <=> C06010 + C00005 + C00080
- `is_product_of` <-- [[molecule.C06010|molecule.C06010]] `KEGG` `database` - C04272 + C00006 <=> C06010 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C04272 + C00006 <=> C06010 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C04272|molecule.C04272]] `KEGG` `database` - C04272 + C00006 <=> C06010 + C00005 + C00080

## External IDs

- `KEGG:R04439`

## Notes

EQUATION: C04272 + C00006 <=> C06010 + C00005 + C00080
