---
entity_id: "reaction.R00573"
entity_type: "reaction"
name: "UTP:L-glutamine amido-ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R00573"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00573"
---

# UTP:L-glutamine amido-ligase (ADP-forming)

`reaction.R00573`

## Static

- Type: `reaction`
- Source: `KEGG:R00573`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + UTP + L-Glutamine + H2O ADP + Orthophosphate + CTP + L-Glutamate

## Biological Role

Catalyzed by pyrG (protein.P0A7E5). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Glutamine (molecule.C00064), UTP (molecule.C00075). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), L-Glutamate (molecule.C00025), CTP (molecule.C00063).

## Annotation

ATP + UTP + L-Glutamine + H2O <=> ADP + Orthophosphate + CTP + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A7E5|protein.P0A7E5]] `KEGG` `database` - via EC:6.3.4.2
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_product_of` <-- [[molecule.C00063|molecule.C00063]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025

## External IDs

- `KEGG:R00573`

## Notes

EQUATION: C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
