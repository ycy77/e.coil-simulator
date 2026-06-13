---
entity_id: "reaction.R00127"
entity_type: "reaction"
name: "ATP:AMP phosphotransferase"
source_database: "KEGG"
source_id: "R00127"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00127"
---

# ATP:AMP phosphotransferase

`reaction.R00127`

## Static

- Type: `reaction`
- Source: `KEGG:R00127`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + AMP 2 ADP

## Biological Role

Catalyzed by adk (protein.P69441). Substrates: ATP (molecule.C00002), AMP (molecule.C00020). Products: ADP (molecule.C00008).

## Annotation

ATP + AMP <=> 2 ADP

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P69441|protein.P69441]] `KEGG` `database` - via EC:2.7.4.3
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00020 <=> 2 C00008
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00020 <=> 2 C00008
- `is_substrate_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00020 <=> 2 C00008

## External IDs

- `KEGG:R00127`

## Notes

EQUATION: C00002 + C00020 <=> 2 C00008
