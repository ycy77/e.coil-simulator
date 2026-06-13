---
entity_id: "reaction.R03416"
entity_type: "reaction"
name: "1-acyl-sn-glycero-3-phosphoethanolamine aldehydohydrolase"
source_database: "KEGG"
source_id: "R03416"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03416"
---

# 1-acyl-sn-glycero-3-phosphoethanolamine aldehydohydrolase

`reaction.R03416`

## Static

- Type: `reaction`
- Source: `KEGG:R03416`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-Acyl-sn-glycero-3-phosphoethanolamine + H2O Fatty acid + sn-Glycero-3-phosphoethanolamine

## Biological Role

Catalyzed by pldB (protein.P07000), tesA (protein.P0ADA1). Substrates: H2O (molecule.C00001), 1-Acyl-sn-glycero-3-phosphoethanolamine (molecule.C04438). Products: Fatty acid (molecule.C00162), sn-Glycero-3-phosphoethanolamine (molecule.C01233).

## Annotation

1-Acyl-sn-glycero-3-phosphoethanolamine + H2O <=> Fatty acid + sn-Glycero-3-phosphoethanolamine

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P07000|protein.P07000]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` <-- [[protein.P0ADA1|protein.P0ADA1]] `KEGG` `database` - via EC:3.1.1.5
- `is_product_of` <-- [[molecule.C00162|molecule.C00162]] `KEGG` `database` - C04438 + C00001 <=> C00162 + C01233
- `is_product_of` <-- [[molecule.C01233|molecule.C01233]] `KEGG` `database` - C04438 + C00001 <=> C00162 + C01233
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04438 + C00001 <=> C00162 + C01233
- `is_substrate_of` <-- [[molecule.C04438|molecule.C04438]] `KEGG` `database` - C04438 + C00001 <=> C00162 + C01233

## External IDs

- `KEGG:R03416`

## Notes

EQUATION: C04438 + C00001 <=> C00162 + C01233
