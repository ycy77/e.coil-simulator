---
entity_id: "reaction.R00215"
entity_type: "reaction"
name: "(R)-malate:NAD+ oxidoreductase (decarboxylating)"
source_database: "KEGG"
source_id: "R00215"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00215"
---

# (R)-malate:NAD+ oxidoreductase (decarboxylating)

`reaction.R00215`

## Static

- Type: `reaction`
- Source: `KEGG:R00215`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(R)-Malate + NAD+ Pyruvate + CO2 + NADH + H+

## Biological Role

Catalyzed by dmlA (protein.P76251). Substrates: NAD+ (molecule.C00003), (R)-Malate (molecule.C00497). Products: NADH (molecule.C00004), CO2 (molecule.C00011), Pyruvate (molecule.C00022), H+ (molecule.C00080).

## Annotation

(R)-Malate + NAD+ <=> Pyruvate + CO2 + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P76251|protein.P76251]] `KEGG` `database` - via EC:1.1.1.83
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00497 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00497 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00497 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00497 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00497 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00497|molecule.C00497]] `KEGG` `database` - C00497 + C00003 <=> C00022 + C00011 + C00004 + C00080

## External IDs

- `KEGG:R00215`

## Notes

EQUATION: C00497 + C00003 <=> C00022 + C00011 + C00004 + C00080
