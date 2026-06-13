---
entity_id: "reaction.R00284"
entity_type: "reaction"
name: "ammonia:acceptor oxidoreductase"
source_database: "KEGG"
source_id: "R00284"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00284"
---

# ammonia:acceptor oxidoreductase

`reaction.R00284`

## Static

- Type: `reaction`
- Source: `KEGG:R00284`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acceptor + Ammonia + H2O Hydroxylamine + Reduced acceptor

## Biological Role

Catalyzed by hcp (protein.P75825). Substrates: H2O (molecule.C00001), Ammonia (molecule.C00014). Products: Hydroxylamine (molecule.C00192).

## Annotation

Acceptor + Ammonia + H2O <=> Hydroxylamine + Reduced acceptor

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P75825|protein.P75825]] `KEGG` `database` - via EC:1.7.99.1
- `is_product_of` <-- [[molecule.C00192|molecule.C00192]] `KEGG` `database` - C00028 + C00014 + C00001 <=> C00192 + C00030
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00028 + C00014 + C00001 <=> C00192 + C00030
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00028 + C00014 + C00001 <=> C00192 + C00030

## External IDs

- `KEGG:R00284`

## Notes

EQUATION: C00028 + C00014 + C00001 <=> C00192 + C00030
