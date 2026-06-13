---
entity_id: "reaction.R04957"
entity_type: "reaction"
name: "hexanoyl-[acyl-carrier protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating)"
source_database: "KEGG"
source_id: "R04957"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04957"
---

# hexanoyl-[acyl-carrier protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating)

`reaction.R04957`

## Static

- Type: `reaction`
- Source: `KEGG:R04957`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hexanoyl-[acp] + Malonyl-[acyl-carrier protein] 3-Oxooctanoyl-[acp] + CO2 + Acyl-carrier protein

## Biological Role

Catalyzed by fabB (protein.P0A953), fabF (protein.P0AAI5). Substrates: Malonyl-[acyl-carrier protein] (molecule.C01209), Hexanoyl-[acp] (molecule.C05749). Products: CO2 (molecule.C00011), Acyl-carrier protein (molecule.C00229), 3-Oxooctanoyl-[acp] (molecule.C05750).

## Annotation

Hexanoyl-[acp] + Malonyl-[acyl-carrier protein] <=> 3-Oxooctanoyl-[acp] + CO2 + Acyl-carrier protein

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A953|protein.P0A953]] `KEGG` `database` - via EC:2.3.1.41
- `catalyzes` <-- [[protein.P0AAI5|protein.P0AAI5]] `KEGG` `database` - via EC:2.3.1.179
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C05749 + C01209 <=> C05750 + C00011 + C00229
- `is_product_of` <-- [[molecule.C00229|molecule.C00229]] `KEGG` `database` - C05749 + C01209 <=> C05750 + C00011 + C00229
- `is_product_of` <-- [[molecule.C05750|molecule.C05750]] `KEGG` `database` - C05749 + C01209 <=> C05750 + C00011 + C00229
- `is_substrate_of` <-- [[molecule.C01209|molecule.C01209]] `KEGG` `database` - C05749 + C01209 <=> C05750 + C00011 + C00229
- `is_substrate_of` <-- [[molecule.C05749|molecule.C05749]] `KEGG` `database` - C05749 + C01209 <=> C05750 + C00011 + C00229

## External IDs

- `KEGG:R04957`

## Notes

EQUATION: C05749 + C01209 <=> C05750 + C00011 + C00229
