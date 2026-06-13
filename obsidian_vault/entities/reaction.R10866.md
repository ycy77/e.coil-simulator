---
entity_id: "reaction.R10866"
entity_type: "reaction"
name: "pyruvate:flavodoxin 2-oxidoreductase (CoA-acetylating)"
source_database: "KEGG"
source_id: "R10866"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10866"
---

# pyruvate:flavodoxin 2-oxidoreductase (CoA-acetylating)

`reaction.R10866`

## Static

- Type: `reaction`
- Source: `KEGG:R10866`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyruvate + CoA + Oxidized flavodoxin Acetyl-CoA + CO2 + Reduced flavodoxin

## Biological Role

Catalyzed by ydbK (protein.P52647). Substrates: CoA (molecule.C00010), Pyruvate (molecule.C00022). Products: CO2 (molecule.C00011), Acetyl-CoA (molecule.C00024).

## Annotation

Pyruvate + CoA + Oxidized flavodoxin <=> Acetyl-CoA + CO2 + Reduced flavodoxin

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P52647|protein.P52647]] `KEGG` `database` - via EC:1.2.8.1
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00022 + C00010 + C02869 <=> C00024 + C00011 + C02745
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00022 + C00010 + C02869 <=> C00024 + C00011 + C02745
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00022 + C00010 + C02869 <=> C00024 + C00011 + C02745
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00022 + C00010 + C02869 <=> C00024 + C00011 + C02745

## External IDs

- `KEGG:R10866`

## Notes

EQUATION: C00022 + C00010 + C02869 <=> C00024 + C00011 + C02745
