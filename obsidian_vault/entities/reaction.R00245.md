---
entity_id: "reaction.R00245"
entity_type: "reaction"
name: "L-glutamate gamma-semialdehyde:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00245"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00245"
---

# L-glutamate gamma-semialdehyde:NAD+ oxidoreductase

`reaction.R00245`

## Static

- Type: `reaction`
- Source: `KEGG:R00245`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Glutamate 5-semialdehyde + NAD+ + H2O L-Glutamate + NADH + H+

## Biological Role

Catalyzed by putA (protein.P09546). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), L-Glutamate 5-semialdehyde (molecule.C01165). Products: NADH (molecule.C00004), L-Glutamate (molecule.C00025), H+ (molecule.C00080).

## Annotation

L-Glutamate 5-semialdehyde + NAD+ + H2O <=> L-Glutamate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P09546|protein.P09546]] `KEGG` `database` - via EC:1.2.1.88
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C01165|molecule.C01165]] `KEGG` `database` - C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080

## External IDs

- `KEGG:R00245`

## Notes

EQUATION: C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080
