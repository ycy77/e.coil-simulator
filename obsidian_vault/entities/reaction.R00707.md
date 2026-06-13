---
entity_id: "reaction.R00707"
entity_type: "reaction"
name: "(S)-1-pyrroline-5-carboxylate:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00707"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00707"
---

# (S)-1-pyrroline-5-carboxylate:NAD+ oxidoreductase

`reaction.R00707`

## Static

- Type: `reaction`
- Source: `KEGG:R00707`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-1-Pyrroline-5-carboxylate + NAD+ + 2 H2O L-Glutamate + NADH + H+

## Biological Role

Catalyzed by putA (protein.P09546). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), (S)-1-Pyrroline-5-carboxylate (molecule.C03912). Products: NADH (molecule.C00004), L-Glutamate (molecule.C00025), H+ (molecule.C00080).

## Annotation

(S)-1-Pyrroline-5-carboxylate + NAD+ + 2 H2O <=> L-Glutamate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P09546|protein.P09546]] `KEGG` `database` - via EC:1.2.1.88
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C03912|molecule.C03912]] `KEGG` `database` - C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080

## External IDs

- `KEGG:R00707`

## Notes

EQUATION: C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080
