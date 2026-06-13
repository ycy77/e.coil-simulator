---
entity_id: "reaction.R04120"
entity_type: "reaction"
name: "peptide-L-methionine:thioredoxin-disulfide S-oxidoreductase [L-methionine (S)-S-oxide-forming]"
source_database: "KEGG"
source_id: "R04120"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04120"
---

# peptide-L-methionine:thioredoxin-disulfide S-oxidoreductase [L-methionine (S)-S-oxide-forming]

`reaction.R04120`

## Static

- Type: `reaction`
- Source: `KEGG:R04120`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Peptide-L-methionine + Thioredoxin disulfide + H2O Peptide-L-methionine (S)-S-oxide + Thioredoxin

## Biological Role

Catalyzed by msrA (protein.P0A744). Substrates: H2O (molecule.C00001).

## Annotation

Peptide-L-methionine + Thioredoxin disulfide + H2O <=> Peptide-L-methionine (S)-S-oxide + Thioredoxin

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P0A744|protein.P0A744]] `KEGG` `database` - via EC:1.8.4.11
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C03023 + C00343 + C00001 <=> C03895 + C00342

## External IDs

- `KEGG:R04120`

## Notes

EQUATION: C03023 + C00343 + C00001 <=> C03895 + C00342
