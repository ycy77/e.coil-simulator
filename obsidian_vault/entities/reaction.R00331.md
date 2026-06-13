---
entity_id: "reaction.R00331"
entity_type: "reaction"
name: "ATP:nucleoside-diphosphate phosphotransferase"
source_database: "KEGG"
source_id: "R00331"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00331"
---

# ATP:nucleoside-diphosphate phosphotransferase

`reaction.R00331`

## Static

- Type: `reaction`
- Source: `KEGG:R00331`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + NDP ADP + Nucleoside triphosphate

## Biological Role

Catalyzed by ndk (protein.P0A763). Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Annotation

ATP + NDP <=> ADP + Nucleoside triphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A763|protein.P0A763]] `KEGG` `database` - via EC:2.7.4.6
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00454 <=> C00008 + C00201
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00454 <=> C00008 + C00201

## External IDs

- `KEGG:R00331`

## Notes

EQUATION: C00002 + C00454 <=> C00008 + C00201
