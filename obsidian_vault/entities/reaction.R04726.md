---
entity_id: "reaction.R04726"
entity_type: "reaction"
name: "dodecanoyl-[acyl-carrier-protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating)"
source_database: "KEGG"
source_id: "R04726"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04726"
---

# dodecanoyl-[acyl-carrier-protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating)

`reaction.R04726`

## Static

- Type: `reaction`
- Source: `KEGG:R04726`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dodecanoyl-[acyl-carrier protein] + Malonyl-[acyl-carrier protein] 3-Oxotetradecanoyl-[acp] + CO2 + Acyl-carrier protein

## Biological Role

Catalyzed by fabB (protein.P0A953), fabF (protein.P0AAI5). Substrates: Malonyl-[acyl-carrier protein] (molecule.C01209), Dodecanoyl-[acyl-carrier protein] (molecule.C05223). Products: CO2 (molecule.C00011), Acyl-carrier protein (molecule.C00229), 3-Oxotetradecanoyl-[acp] (molecule.C05759).

## Annotation

Dodecanoyl-[acyl-carrier protein] + Malonyl-[acyl-carrier protein] <=> 3-Oxotetradecanoyl-[acp] + CO2 + Acyl-carrier protein

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A953|protein.P0A953]] `KEGG` `database` - via EC:2.3.1.41
- `catalyzes` <-- [[protein.P0AAI5|protein.P0AAI5]] `KEGG` `database` - via EC:2.3.1.179
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C05223 + C01209 <=> C05759 + C00011 + C00229
- `is_product_of` <-- [[molecule.C00229|molecule.C00229]] `KEGG` `database` - C05223 + C01209 <=> C05759 + C00011 + C00229
- `is_product_of` <-- [[molecule.C05759|molecule.C05759]] `KEGG` `database` - C05223 + C01209 <=> C05759 + C00011 + C00229
- `is_substrate_of` <-- [[molecule.C01209|molecule.C01209]] `KEGG` `database` - C05223 + C01209 <=> C05759 + C00011 + C00229
- `is_substrate_of` <-- [[molecule.C05223|molecule.C05223]] `KEGG` `database` - C05223 + C01209 <=> C05759 + C00011 + C00229

## External IDs

- `KEGG:R04726`

## Notes

EQUATION: C05223 + C01209 <=> C05759 + C00011 + C00229
