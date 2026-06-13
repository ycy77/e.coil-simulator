---
entity_id: "reaction.R04111"
entity_type: "reaction"
name: "protein-N(pi)-phosphohistidine:maltose 6'-phosphotransferase"
source_database: "KEGG"
source_id: "R04111"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04111"
---

# protein-N(pi)-phosphohistidine:maltose 6'-phosphotransferase

`reaction.R04111`

## Static

- Type: `reaction`
- Source: `KEGG:R04111`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein N(pi)-phospho-L-histidine + Maltose Protein histidine + Maltose 6'-phosphate

## Biological Role

Catalyzed by glvB (gene.b3682), glvC (gene.b3683), malX (protein.P19642). Substrates: Maltose (molecule.C00208). Products: Maltose 6'-phosphate (molecule.C02995).

## Annotation

Protein N(pi)-phospho-L-histidine + Maltose <=> Protein histidine + Maltose 6'-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[gene.b3682|gene.b3682]] `KEGG` `database` - via EC:2.7.1.208
- `catalyzes` <-- [[gene.b3683|gene.b3683]] `KEGG` `database` - via EC:2.7.1.208
- `catalyzes` <-- [[protein.P19642|protein.P19642]] `KEGG` `database` - via EC:2.7.1.208
- `is_product_of` <-- [[molecule.C02995|molecule.C02995]] `KEGG` `database` - C04261 + C00208 <=> C00615 + C02995
- `is_substrate_of` <-- [[molecule.C00208|molecule.C00208]] `KEGG` `database` - C04261 + C00208 <=> C00615 + C02995

## External IDs

- `KEGG:R04111`

## Notes

EQUATION: C04261 + C00208 <=> C00615 + C02995
