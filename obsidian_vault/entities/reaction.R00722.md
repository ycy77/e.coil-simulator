---
entity_id: "reaction.R00722"
entity_type: "reaction"
name: "ATP:IDP phosphotransferase"
source_database: "KEGG"
source_id: "R00722"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00722"
---

# ATP:IDP phosphotransferase

`reaction.R00722`

## Static

- Type: `reaction`
- Source: `KEGG:R00722`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + IDP ADP + ITP

## Biological Role

Catalyzed by ndk (protein.P0A763). Substrates: ATP (molecule.C00002), IDP (molecule.C00104). Products: ADP (molecule.C00008), ITP (molecule.C00081).

## Annotation

ATP + IDP <=> ADP + ITP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A763|protein.P0A763]] `KEGG` `database` - via EC:2.7.4.6
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00104 <=> C00008 + C00081
- `is_product_of` <-- [[molecule.C00081|molecule.C00081]] `KEGG` `database` - C00002 + C00104 <=> C00008 + C00081
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00104 <=> C00008 + C00081
- `is_substrate_of` <-- [[molecule.C00104|molecule.C00104]] `KEGG` `database` - C00002 + C00104 <=> C00008 + C00081

## External IDs

- `KEGG:R00722`

## Notes

EQUATION: C00002 + C00104 <=> C00008 + C00081
