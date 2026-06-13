---
entity_id: "reaction.R00214"
entity_type: "reaction"
name: "(S)-malate:NAD+ oxidoreductase (decarboxylating)"
source_database: "KEGG"
source_id: "R00214"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00214"
---

# (S)-malate:NAD+ oxidoreductase (decarboxylating)

`reaction.R00214`

## Static

- Type: `reaction`
- Source: `KEGG:R00214`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-Malate + NAD+ Pyruvate + CO2 + NADH + H+

## Biological Role

Catalyzed by maeA (protein.P26616). Substrates: NAD+ (molecule.C00003), (S)-Malate (molecule.C00149). Products: NADH (molecule.C00004), CO2 (molecule.C00011), Pyruvate (molecule.C00022), H+ (molecule.C00080).

## Annotation

(S)-Malate + NAD+ <=> Pyruvate + CO2 + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P26616|protein.P26616]] `KEGG` `database` - via EC:1.1.1.38
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00149 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00149 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00149 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00149 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00149 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `KEGG` `database` - C00149 + C00003 <=> C00022 + C00011 + C00004 + C00080

## External IDs

- `KEGG:R00214`

## Notes

EQUATION: C00149 + C00003 <=> C00022 + C00011 + C00004 + C00080
