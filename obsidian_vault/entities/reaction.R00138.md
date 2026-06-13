---
entity_id: "reaction.R00138"
entity_type: "reaction"
name: "triphosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R00138"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00138"
---

# triphosphate phosphohydrolase

`reaction.R00138`

## Static

- Type: `reaction`
- Source: `KEGG:R00138`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Triphosphate + H2O Diphosphate + Orthophosphate

## Biological Role

Catalyzed by ygiF (protein.P30871). Substrates: H2O (molecule.C00001), Triphosphate (molecule.C00536). Products: Orthophosphate (molecule.C00009), Diphosphate (molecule.C00013).

## Annotation

Triphosphate + H2O <=> Diphosphate + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P30871|protein.P30871]] `KEGG` `database` - via EC:3.6.1.25
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00536 + C00001 <=> C00013 + C00009
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00536 + C00001 <=> C00013 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00536 + C00001 <=> C00013 + C00009
- `is_substrate_of` <-- [[molecule.C00536|molecule.C00536]] `KEGG` `database` - C00536 + C00001 <=> C00013 + C00009

## External IDs

- `KEGG:R00138`

## Notes

EQUATION: C00536 + C00001 <=> C00013 + C00009
