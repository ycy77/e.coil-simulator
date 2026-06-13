---
entity_id: "reaction.R00162"
entity_type: "reaction"
name: "ATP:protein phosphotransferase;"
source_database: "KEGG"
source_id: "R00162"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00162"
---

# ATP:protein phosphotransferase;

`reaction.R00162`

## Static

- Type: `reaction`
- Source: `KEGG:R00162`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Protein ADP + Phosphoprotein

## Biological Role

Catalyzed by hipA (protein.P23874). Substrates: ATP (molecule.C00002), Protein (molecule.C00017). Products: ADP (molecule.C00008).

## Annotation

ATP + Protein <=> ADP + Phosphoprotein

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P23874|protein.P23874]] `KEGG` `database` - via EC:2.7.11.1
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00017 <=> C00008 + C00562
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00017 <=> C00008 + C00562
- `is_substrate_of` <-- [[molecule.C00017|molecule.C00017]] `KEGG` `database` - C00002 + C00017 <=> C00008 + C00562

## External IDs

- `KEGG:R00162`

## Notes

EQUATION: C00002 + C00017 <=> C00008 + C00562
