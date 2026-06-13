---
entity_id: "reaction.R05820"
entity_type: "reaction"
name: "protein-N(pi)-phosphohistidine:D-sorbitol 6-phosphotransferase"
source_database: "KEGG"
source_id: "R05820"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05820"
---

# protein-N(pi)-phosphohistidine:D-sorbitol 6-phosphotransferase

`reaction.R05820`

## Static

- Type: `reaction`
- Source: `KEGG:R05820`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein N(pi)-phospho-L-histidine + D-Sorbitol Protein histidine + Sorbitol 6-phosphate

## Biological Role

Catalyzed by srlB (protein.P05706), srlE (protein.P56580). Substrates: D-Sorbitol (molecule.C00794). Products: Sorbitol 6-phosphate (molecule.C01096).

## Annotation

Protein N(pi)-phospho-L-histidine + D-Sorbitol <=> Protein histidine + Sorbitol 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P05706|protein.P05706]] `KEGG` `database` - via EC:2.7.1.198
- `catalyzes` <-- [[protein.P56580|protein.P56580]] `KEGG` `database` - via EC:2.7.1.198
- `is_product_of` <-- [[molecule.C01096|molecule.C01096]] `KEGG` `database` - C04261 + C00794 <=> C00615 + C01096
- `is_substrate_of` <-- [[molecule.C00794|molecule.C00794]] `KEGG` `database` - C04261 + C00794 <=> C00615 + C01096

## External IDs

- `KEGG:R05820`

## Notes

EQUATION: C04261 + C00794 <=> C00615 + C01096
