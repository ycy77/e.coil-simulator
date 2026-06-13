---
entity_id: "reaction.R00339"
entity_type: "reaction"
name: "(R,R)-tartrate hydro-lyase (oxaloacetate-forming)"
source_database: "KEGG"
source_id: "R00339"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00339"
---

# (R,R)-tartrate hydro-lyase (oxaloacetate-forming)

`reaction.R00339`

## Static

- Type: `reaction`
- Source: `KEGG:R00339`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(R,R)-Tartaric acid Oxaloacetate + H2O

## Biological Role

Catalyzed by ttdA (protein.P05847), ttdB (protein.P0AC35). Substrates: (R,R)-Tartaric acid (molecule.C00898). Products: H2O (molecule.C00001), Oxaloacetate (molecule.C00036).

## Annotation

(R,R)-Tartaric acid <=> Oxaloacetate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P05847|protein.P05847]] `KEGG` `database` - via EC:4.2.1.32
- `catalyzes` <-- [[protein.P0AC35|protein.P0AC35]] `KEGG` `database` - via EC:4.2.1.32
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00898 <=> C00036 + C00001
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00898 <=> C00036 + C00001
- `is_substrate_of` <-- [[molecule.C00898|molecule.C00898]] `KEGG` `database` - C00898 <=> C00036 + C00001

## External IDs

- `KEGG:R00339`

## Notes

EQUATION: C00898 <=> C00036 + C00001
