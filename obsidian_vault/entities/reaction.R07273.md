---
entity_id: "reaction.R07273"
entity_type: "reaction"
name: "solanesyl-diphosphate:4-hydroxybenzoate nonaprenyltransferase"
source_database: "KEGG"
source_id: "R07273"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07273"
---

# solanesyl-diphosphate:4-hydroxybenzoate nonaprenyltransferase

`reaction.R07273`

## Static

- Type: `reaction`
- Source: `KEGG:R07273`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

all-trans-Nonaprenyl diphosphate + 4-Hydroxybenzoate Diphosphate + 3-Nonaprenyl-4-hydroxybenzoate

## Biological Role

Catalyzed by ubiA (protein.P0AGK1). Substrates: 4-Hydroxybenzoate (molecule.C00156), all-trans-Nonaprenyl diphosphate (molecule.C04145). Products: Diphosphate (molecule.C00013).

## Annotation

all-trans-Nonaprenyl diphosphate + 4-Hydroxybenzoate <=> Diphosphate + 3-Nonaprenyl-4-hydroxybenzoate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AGK1|protein.P0AGK1]] `KEGG` `database` - via EC:2.5.1.39
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C04145 + C00156 <=> C00013 + C03885
- `is_substrate_of` <-- [[molecule.C00156|molecule.C00156]] `KEGG` `database` - C04145 + C00156 <=> C00013 + C03885
- `is_substrate_of` <-- [[molecule.C04145|molecule.C04145]] `KEGG` `database` - C04145 + C00156 <=> C00013 + C03885

## External IDs

- `KEGG:R07273`

## Notes

EQUATION: C04145 + C00156 <=> C00013 + C03885
