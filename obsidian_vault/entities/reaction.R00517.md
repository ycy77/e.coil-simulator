---
entity_id: "reaction.R00517"
entity_type: "reaction"
name: "GTP:cytidine 5'-phosphotransferase"
source_database: "KEGG"
source_id: "R00517"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00517"
---

# GTP:cytidine 5'-phosphotransferase

`reaction.R00517`

## Static

- Type: `reaction`
- Source: `KEGG:R00517`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + Cytidine GDP + CMP

## Biological Role

Catalyzed by udk (protein.P0A8F4). Substrates: GTP (molecule.C00044), Cytidine (molecule.C00475). Products: GDP (molecule.C00035), CMP (molecule.C00055).

## Annotation

GTP + Cytidine <=> GDP + CMP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A8F4|protein.P0A8F4]] `KEGG` `database` - via EC:2.7.1.48
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `KEGG` `database` - C00044 + C00475 <=> C00035 + C00055
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `KEGG` `database` - C00044 + C00475 <=> C00035 + C00055
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 + C00475 <=> C00035 + C00055
- `is_substrate_of` <-- [[molecule.C00475|molecule.C00475]] `KEGG` `database` - C00044 + C00475 <=> C00035 + C00055

## External IDs

- `KEGG:R00517`

## Notes

EQUATION: C00044 + C00475 <=> C00035 + C00055
