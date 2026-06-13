---
entity_id: "reaction.R03417"
entity_type: "reaction"
name: "L-2-lysophosphatidylethanolamine aldehydohydrolase"
source_database: "KEGG"
source_id: "R03417"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03417"
---

# L-2-lysophosphatidylethanolamine aldehydohydrolase

`reaction.R03417`

## Static

- Type: `reaction`
- Source: `KEGG:R03417`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Acyl-sn-glycero-3-phosphoethanolamine + H2O Fatty acid + sn-Glycero-3-phosphoethanolamine

## Biological Role

Catalyzed by pldB (protein.P07000), tesA (protein.P0ADA1). Substrates: H2O (molecule.C00001), 2-Acyl-sn-glycero-3-phosphoethanolamine (molecule.C05973). Products: Fatty acid (molecule.C00162), sn-Glycero-3-phosphoethanolamine (molecule.C01233).

## Annotation

2-Acyl-sn-glycero-3-phosphoethanolamine + H2O <=> Fatty acid + sn-Glycero-3-phosphoethanolamine

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P07000|protein.P07000]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` <-- [[protein.P0ADA1|protein.P0ADA1]] `KEGG` `database` - via EC:3.1.1.5
- `is_product_of` <-- [[molecule.C00162|molecule.C00162]] `KEGG` `database` - C05973 + C00001 <=> C00162 + C01233
- `is_product_of` <-- [[molecule.C01233|molecule.C01233]] `KEGG` `database` - C05973 + C00001 <=> C00162 + C01233
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05973 + C00001 <=> C00162 + C01233
- `is_substrate_of` <-- [[molecule.C05973|molecule.C05973]] `KEGG` `database` - C05973 + C00001 <=> C00162 + C01233

## External IDs

- `KEGG:R03417`

## Notes

EQUATION: C05973 + C00001 <=> C00162 + C01233
