---
entity_id: "reaction.R13003"
entity_type: "reaction"
name: "ADP-L-glycero-beta-D-manno-heptose:an alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[lipid A] 5-alpha-heptosyltransferase"
source_database: "KEGG"
source_id: "R13003"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R13003"
---

# ADP-L-glycero-beta-D-manno-heptose:an alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[lipid A] 5-alpha-heptosyltransferase

`reaction.R13003`

## Static

- Type: `reaction`
- Source: `KEGG:R13003`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADP-L-glycero-beta-D-manno-heptose + G00651 ADP + G06499

## Biological Role

Catalyzed by waaC (protein.P24173). Substrates: ADP-L-glycero-beta-D-manno-heptose (molecule.C06398). Products: ADP (molecule.C00008).

## Annotation

ADP-L-glycero-beta-D-manno-heptose + G00651 <=> ADP + G06499

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P24173|protein.P24173]] `KEGG` `database` - via EC:2.4.99.23
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C06398 + G00651 <=> C00008 + G06499
- `is_substrate_of` <-- [[molecule.C06398|molecule.C06398]] `KEGG` `database` - C06398 + G00651 <=> C00008 + G06499

## External IDs

- `KEGG:R13003`

## Notes

EQUATION: C06398 + G00651 <=> C00008 + G06499
