---
entity_id: "reaction.R00698"
entity_type: "reaction"
name: "L-phenylalanine:oxygen oxidoreductase (decarboxylating)"
source_database: "KEGG"
source_id: "R00698"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00698"
---

# L-phenylalanine:oxygen oxidoreductase (decarboxylating)

`reaction.R00698`

## Static

- Type: `reaction`
- Source: `KEGG:R00698`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Phenylalanine + Oxygen 2-Phenylacetamide + CO2

## Biological Role

Catalyzed by katG (protein.P13029). Substrates: Oxygen (molecule.C00007), L-Phenylalanine (molecule.C00079). Products: CO2 (molecule.C00011), 2-Phenylacetamide (molecule.C02505).

## Annotation

L-Phenylalanine + Oxygen <=> 2-Phenylacetamide + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P13029|protein.P13029]] `KEGG` `database` - via EC:1.11.1.21
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00079 + C00007 <=> C02505 + C00011
- `is_product_of` <-- [[molecule.C02505|molecule.C02505]] `KEGG` `database` - C00079 + C00007 <=> C02505 + C00011
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00079 + C00007 <=> C02505 + C00011
- `is_substrate_of` <-- [[molecule.C00079|molecule.C00079]] `KEGG` `database` - C00079 + C00007 <=> C02505 + C00011

## External IDs

- `KEGG:R00698`

## Notes

EQUATION: C00079 + C00007 <=> C02505 + C00011
