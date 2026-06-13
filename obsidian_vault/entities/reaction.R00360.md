---
entity_id: "reaction.R00360"
entity_type: "reaction"
name: "(S)-malate:oxygen oxidoreductase"
source_database: "KEGG"
source_id: "R00360"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00360"
---

# (S)-malate:oxygen oxidoreductase

`reaction.R00360`

## Static

- Type: `reaction`
- Source: `KEGG:R00360`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-Malate + Oxygen Oxaloacetate + Hydrogen peroxide

## Biological Role

Catalyzed by mqo (protein.P33940). Substrates: Oxygen (molecule.C00007), (S)-Malate (molecule.C00149). Products: Hydrogen peroxide (molecule.C00027), Oxaloacetate (molecule.C00036).

## Annotation

(S)-Malate + Oxygen <=> Oxaloacetate + Hydrogen peroxide

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33940|protein.P33940]] `KEGG` `database` - via EC:1.1.5.4
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00149 + C00007 <=> C00036 + C00027
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00149 + C00007 <=> C00036 + C00027
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00149 + C00007 <=> C00036 + C00027
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `KEGG` `database` - C00149 + C00007 <=> C00036 + C00027

## External IDs

- `KEGG:R00360`

## Notes

EQUATION: C00149 + C00007 <=> C00036 + C00027
