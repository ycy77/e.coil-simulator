---
entity_id: "reaction.R00708"
entity_type: "reaction"
name: "(S)-1-pyrroline-5-carboxylate:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R00708"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00708"
---

# (S)-1-pyrroline-5-carboxylate:NADP+ oxidoreductase

`reaction.R00708`

## Static

- Type: `reaction`
- Source: `KEGG:R00708`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-1-Pyrroline-5-carboxylate + NADP+ + 2 H2O L-Glutamate + NADPH + H+

## Biological Role

Catalyzed by putA (protein.P09546). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), (S)-1-Pyrroline-5-carboxylate (molecule.C03912). Products: NADPH (molecule.C00005), L-Glutamate (molecule.C00025), H+ (molecule.C00080).

## Annotation

(S)-1-Pyrroline-5-carboxylate + NADP+ + 2 H2O <=> L-Glutamate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P09546|protein.P09546]] `KEGG` `database` - via EC:1.2.1.88
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C03912|molecule.C03912]] `KEGG` `database` - C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080

## External IDs

- `KEGG:R00708`

## Notes

EQUATION: C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080
