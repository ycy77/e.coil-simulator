---
entity_id: "reaction.R11485"
entity_type: "reaction"
name: "flavodoxin:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R11485"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11485"
---

# flavodoxin:NADP+ oxidoreductase

`reaction.R11485`

## Static

- Type: `reaction`
- Source: `KEGG:R11485`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Reduced flavodoxin + NADP+ Oxidized flavodoxin + NADPH + H+

## Biological Role

Catalyzed by fpr (protein.P28861). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Annotation

Reduced flavodoxin + NADP+ <=> Oxidized flavodoxin + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P28861|protein.P28861]] `KEGG` `database` - via EC:1.19.1.1
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C02745 + C00006 <=> C02869 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C02745 + C00006 <=> C02869 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C02745 + C00006 <=> C02869 + C00005 + C00080

## External IDs

- `KEGG:R11485`

## Notes

EQUATION: C02745 + C00006 <=> C02869 + C00005 + C00080
