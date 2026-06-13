---
entity_id: "reaction.R03145"
entity_type: "reaction"
name: "pyruvate:ubiquinone oxidoreductase"
source_database: "KEGG"
source_id: "R03145"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03145"
---

# pyruvate:ubiquinone oxidoreductase

`reaction.R03145`

## Static

- Type: `reaction`
- Source: `KEGG:R03145`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyruvate + Ubiquinone + H2O Acetate + Ubiquinol + CO2

## Biological Role

Catalyzed by poxB (protein.P07003). Substrates: H2O (molecule.C00001), Pyruvate (molecule.C00022), Ubiquinone (molecule.C00399). Products: CO2 (molecule.C00011), Acetate (molecule.C00033), Ubiquinol (molecule.C00390).

## Annotation

Pyruvate + Ubiquinone + H2O <=> Acetate + Ubiquinol + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P07003|protein.P07003]] `KEGG` `database` - via EC:1.2.5.1
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `KEGG` `database` - C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011
- `is_substrate_of` <-- [[molecule.C00399|molecule.C00399]] `KEGG` `database` - C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011

## External IDs

- `KEGG:R03145`

## Notes

EQUATION: C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011
