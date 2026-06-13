---
entity_id: "reaction.R00662"
entity_type: "reaction"
name: "uridine triphosphate pyrophosphohydrolase"
source_database: "KEGG"
source_id: "R00662"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00662"
---

# uridine triphosphate pyrophosphohydrolase

`reaction.R00662`

## Static

- Type: `reaction`
- Source: `KEGG:R00662`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UTP + H2O UMP + Diphosphate

## Biological Role

Catalyzed by mazG (protein.P0AEY3). Substrates: H2O (molecule.C00001), UTP (molecule.C00075). Products: Diphosphate (molecule.C00013), UMP (molecule.C00105).

## Annotation

UTP + H2O <=> UMP + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEY3|protein.P0AEY3]] `KEGG` `database` - via EC:3.6.1.9
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00075 + C00001 <=> C00105 + C00013
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `KEGG` `database` - C00075 + C00001 <=> C00105 + C00013
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00075 + C00001 <=> C00105 + C00013
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00075 + C00001 <=> C00105 + C00013

## External IDs

- `KEGG:R00662`

## Notes

EQUATION: C00075 + C00001 <=> C00105 + C00013
