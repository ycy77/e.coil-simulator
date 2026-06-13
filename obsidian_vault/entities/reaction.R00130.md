---
entity_id: "reaction.R00130"
entity_type: "reaction"
name: "ATP:dephospho-CoA 3'-phosphotransferase"
source_database: "KEGG"
source_id: "R00130"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00130"
---

# ATP:dephospho-CoA 3'-phosphotransferase

`reaction.R00130`

## Static

- Type: `reaction`
- Source: `KEGG:R00130`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Dephospho-CoA ADP + CoA

## Biological Role

Catalyzed by coaE (protein.P0A6I9). Substrates: ATP (molecule.C00002), Dephospho-CoA (molecule.C00882). Products: ADP (molecule.C00008), CoA (molecule.C00010).

## Annotation

ATP + Dephospho-CoA <=> ADP + CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6I9|protein.P0A6I9]] `KEGG` `database` - via EC:2.7.1.24
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00882 <=> C00008 + C00010
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00002 + C00882 <=> C00008 + C00010
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00882 <=> C00008 + C00010
- `is_substrate_of` <-- [[molecule.C00882|molecule.C00882]] `KEGG` `database` - C00002 + C00882 <=> C00008 + C00010

## External IDs

- `KEGG:R00130`

## Notes

EQUATION: C00002 + C00882 <=> C00008 + C00010
