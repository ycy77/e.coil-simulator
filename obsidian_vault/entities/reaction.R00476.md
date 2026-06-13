---
entity_id: "reaction.R00476"
entity_type: "reaction"
name: "glycolate:acceptor 2-oxidoreductase"
source_database: "KEGG"
source_id: "R00476"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00476"
---

# glycolate:acceptor 2-oxidoreductase

`reaction.R00476`

## Static

- Type: `reaction`
- Source: `KEGG:R00476`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glycolate + Acceptor Glyoxylate + Reduced acceptor

## Biological Role

Catalyzed by glcD (protein.P0AEP9), glcE (protein.P52073), glcF (protein.P52074). Substrates: Glycolate (molecule.C00160). Products: Glyoxylate (molecule.C00048).

## Annotation

Glycolate + Acceptor <=> Glyoxylate + Reduced acceptor

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEP9|protein.P0AEP9]] `KEGG` `database` - via EC:1.1.99.14
- `catalyzes` <-- [[protein.P52073|protein.P52073]] `KEGG` `database` - via EC:1.1.99.14
- `catalyzes` <-- [[protein.P52074|protein.P52074]] `KEGG` `database` - via EC:1.1.99.14
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `KEGG` `database` - C00160 + C00028 <=> C00048 + C00030
- `is_substrate_of` <-- [[molecule.C00160|molecule.C00160]] `KEGG` `database` - C00160 + C00028 <=> C00048 + C00030

## External IDs

- `KEGG:R00476`

## Notes

EQUATION: C00160 + C00028 <=> C00048 + C00030
