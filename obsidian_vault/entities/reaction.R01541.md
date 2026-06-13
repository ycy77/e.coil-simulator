---
entity_id: "reaction.R01541"
entity_type: "reaction"
name: "ATP:2-dehydro-3-deoxy-D-gluconate 6-phosphotransferase"
source_database: "KEGG"
source_id: "R01541"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01541"
---

# ATP:2-dehydro-3-deoxy-D-gluconate 6-phosphotransferase

`reaction.R01541`

## Static

- Type: `reaction`
- Source: `KEGG:R01541`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + 2-Dehydro-3-deoxy-D-gluconate ADP + 2-Dehydro-3-deoxy-6-phospho-D-gluconate

## Biological Role

Catalyzed by kdgK (protein.P37647). Substrates: ATP (molecule.C00002), 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204). Products: ADP (molecule.C00008), 2-Dehydro-3-deoxy-6-phospho-D-gluconate (molecule.C04442).

## Annotation

ATP + 2-Dehydro-3-deoxy-D-gluconate <=> ADP + 2-Dehydro-3-deoxy-6-phospho-D-gluconate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37647|protein.P37647]] `KEGG` `database` - via EC:2.7.1.45
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00204 <=> C00008 + C04442
- `is_product_of` <-- [[molecule.C04442|molecule.C04442]] `KEGG` `database` - C00002 + C00204 <=> C00008 + C04442
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00204 <=> C00008 + C04442
- `is_substrate_of` <-- [[molecule.C00204|molecule.C00204]] `KEGG` `database` - C00002 + C00204 <=> C00008 + C04442

## External IDs

- `KEGG:R01541`

## Notes

EQUATION: C00002 + C00204 <=> C00008 + C04442
