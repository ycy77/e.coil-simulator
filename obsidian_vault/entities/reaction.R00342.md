---
entity_id: "reaction.R00342"
entity_type: "reaction"
name: "(S)-malate:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00342"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00342"
---

# (S)-malate:NAD+ oxidoreductase

`reaction.R00342`

## Static

- Type: `reaction`
- Source: `KEGG:R00342`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-Malate + NAD+ Oxaloacetate + NADH + H+

## Biological Role

Catalyzed by mdh (protein.P61889). Substrates: NAD+ (molecule.C00003), (S)-Malate (molecule.C00149). Products: NADH (molecule.C00004), Oxaloacetate (molecule.C00036), H+ (molecule.C00080).

## Annotation

(S)-Malate + NAD+ <=> Oxaloacetate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P61889|protein.P61889]] `KEGG` `database` - via EC:1.1.1.37
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00149 + C00003 <=> C00036 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00149 + C00003 <=> C00036 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00149 + C00003 <=> C00036 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00149 + C00003 <=> C00036 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `KEGG` `database` - C00149 + C00003 <=> C00036 + C00004 + C00080

## External IDs

- `KEGG:R00342`

## Notes

EQUATION: C00149 + C00003 <=> C00036 + C00004 + C00080
