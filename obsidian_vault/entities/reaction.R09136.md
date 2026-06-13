---
entity_id: "reaction.R09136"
entity_type: "reaction"
name: "2,3,5-trichlorodienelactone lactonohydrolase"
source_database: "KEGG"
source_id: "R09136"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09136"
---

# 2,3,5-trichlorodienelactone lactonohydrolase

`reaction.R09136`

## Static

- Type: `reaction`
- Source: `KEGG:R09136`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2,3,5-Trichlorodienelactone + H2O 2,3,5-Trichloromaleylacetate

## Biological Role

Catalyzed by ysgA (protein.P56262). Substrates: H2O (molecule.C00001), 2,3,5-Trichlorodienelactone (molecule.C18242). Products: 2,3,5-Trichloromaleylacetate (molecule.C18243).

## Annotation

2,3,5-Trichlorodienelactone + H2O <=> 2,3,5-Trichloromaleylacetate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P56262|protein.P56262]] `KEGG` `database` - via EC:3.1.1.45
- `is_product_of` <-- [[molecule.C18243|molecule.C18243]] `KEGG` `database` - C18242 + C00001 <=> C18243
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C18242 + C00001 <=> C18243
- `is_substrate_of` <-- [[molecule.C18242|molecule.C18242]] `KEGG` `database` - C18242 + C00001 <=> C18243

## External IDs

- `KEGG:R09136`

## Notes

EQUATION: C18242 + C00001 <=> C18243
