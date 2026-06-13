---
entity_id: "reaction.R00670"
entity_type: "reaction"
name: "L-ornithine carboxy-lyase (putrescine-forming)"
source_database: "KEGG"
source_id: "R00670"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00670"
---

# L-ornithine carboxy-lyase (putrescine-forming)

`reaction.R00670`

## Static

- Type: `reaction`
- Source: `KEGG:R00670`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Ornithine Putrescine + CO2

## Biological Role

Catalyzed by speC (protein.P21169), speF (protein.P24169). Substrates: L-Ornithine (molecule.C00077). Products: CO2 (molecule.C00011), Putrescine (molecule.C00134).

## Annotation

L-Ornithine <=> Putrescine + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21169|protein.P21169]] `KEGG` `database` - via EC:4.1.1.17
- `catalyzes` <-- [[protein.P24169|protein.P24169]] `KEGG` `database` - via EC:4.1.1.17
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00077 <=> C00134 + C00011
- `is_product_of` <-- [[molecule.C00134|molecule.C00134]] `KEGG` `database` - C00077 <=> C00134 + C00011
- `is_substrate_of` <-- [[molecule.C00077|molecule.C00077]] `KEGG` `database` - C00077 <=> C00134 + C00011

## External IDs

- `KEGG:R00670`

## Notes

EQUATION: C00077 <=> C00134 + C00011
