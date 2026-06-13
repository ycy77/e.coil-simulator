---
entity_id: "reaction.R00361"
entity_type: "reaction"
name: "(S)-malate:quinone oxidoreductase"
source_database: "KEGG"
source_id: "R00361"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00361"
---

# (S)-malate:quinone oxidoreductase

`reaction.R00361`

## Static

- Type: `reaction`
- Source: `KEGG:R00361`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-Malate + Quinone Oxaloacetate + Hydroquinone

## Biological Role

Catalyzed by mqo (protein.P33940). Substrates: (S)-Malate (molecule.C00149). Products: Oxaloacetate (molecule.C00036).

## Annotation

(S)-Malate + Quinone <=> Oxaloacetate + Hydroquinone

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P33940|protein.P33940]] `KEGG` `database` - via EC:1.1.5.4
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00149 + C15602 <=> C00036 + C15603
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `KEGG` `database` - C00149 + C15602 <=> C00036 + C15603

## External IDs

- `KEGG:R00361`

## Notes

EQUATION: C00149 + C15602 <=> C00036 + C15603
