---
entity_id: "reaction.R00267"
entity_type: "reaction"
name: "isocitrate:NADP+ oxidoreductase (decarboxylating)"
source_database: "KEGG"
source_id: "R00267"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00267"
---

# isocitrate:NADP+ oxidoreductase (decarboxylating)

`reaction.R00267`

## Static

- Type: `reaction`
- Source: `KEGG:R00267`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Isocitrate + NADP+ 2-Oxoglutarate + CO2 + NADPH + H+

## Biological Role

Catalyzed by icd (protein.P08200). Substrates: NADP+ (molecule.C00006), Isocitrate (molecule.C00311). Products: NADPH (molecule.C00005), CO2 (molecule.C00011), 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080).

## Annotation

Isocitrate + NADP+ <=> 2-Oxoglutarate + CO2 + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P08200|protein.P08200]] `KEGG` `database` - via EC:1.1.1.42
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00311|molecule.C00311]] `KEGG` `database` - C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080

## External IDs

- `KEGG:R00267`

## Notes

EQUATION: C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080
