---
entity_id: "reaction.R00390"
entity_type: "reaction"
name: "long-chain-fatty-acid:CoA ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R00390"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00390"
---

# long-chain-fatty-acid:CoA ligase (AMP-forming)

`reaction.R00390`

## Static

- Type: `reaction`
- Source: `KEGG:R00390`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Long-chain fatty acid + CoA AMP + Diphosphate + Long-chain acyl-CoA

## Biological Role

Catalyzed by fadD (protein.P69451). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Long-chain fatty acid (molecule.C00638). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), Long-chain acyl-CoA (molecule.C02843).

## Annotation

ATP + Long-chain fatty acid + CoA <=> AMP + Diphosphate + Long-chain acyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P69451|protein.P69451]] `KEGG` `database` - via EC:6.2.1.3
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843
- `is_product_of` <-- [[molecule.C02843|molecule.C02843]] `KEGG` `database` - C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843
- `is_substrate_of` <-- [[molecule.C00638|molecule.C00638]] `KEGG` `database` - C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843

## External IDs

- `KEGG:R00390`

## Notes

EQUATION: C00002 + C00638 + C00010 <=> C00020 + C00013 + C02843
