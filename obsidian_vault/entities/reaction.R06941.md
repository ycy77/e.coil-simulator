---
entity_id: "reaction.R06941"
entity_type: "reaction"
name: "(S)-3-hydroxyacyl-CoA:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R06941"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06941"
---

# (S)-3-hydroxyacyl-CoA:NAD+ oxidoreductase

`reaction.R06941`

## Static

- Type: `reaction`
- Source: `KEGG:R06941`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(3S)-3-Hydroxyadipyl-CoA + NAD+ 3-Oxoadipyl-CoA + NADH + H+

## Biological Role

Catalyzed by fadB (protein.P21177), paaH (protein.P76083), fadJ (protein.P77399). Substrates: NAD+ (molecule.C00003), (3S)-3-Hydroxyadipyl-CoA (molecule.C14145). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-Oxoadipyl-CoA (molecule.C02232).

## Annotation

(3S)-3-Hydroxyadipyl-CoA + NAD+ <=> 3-Oxoadipyl-CoA + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `KEGG` `database` - via EC:1.1.1.35
- `catalyzes` <-- [[protein.P76083|protein.P76083]] `KEGG` `database` - via EC:1.1.1.157
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `KEGG` `database` - via EC:1.1.1.35
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C14145 + C00003 <=> C02232 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C14145 + C00003 <=> C02232 + C00004 + C00080
- `is_product_of` <-- [[molecule.C02232|molecule.C02232]] `KEGG` `database` - C14145 + C00003 <=> C02232 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C14145 + C00003 <=> C02232 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C14145|molecule.C14145]] `KEGG` `database` - C14145 + C00003 <=> C02232 + C00004 + C00080

## External IDs

- `KEGG:R06941`

## Notes

EQUATION: C14145 + C00003 <=> C02232 + C00004 + C00080
