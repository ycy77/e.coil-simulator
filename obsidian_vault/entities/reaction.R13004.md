---
entity_id: "reaction.R13004"
entity_type: "reaction"
name: "ADP-L-glycero-beta-D-manno-heptose:an alpha-L-glycero-D-manno-heptosyl-(1->5)-[alpha-Kdo-(2->4)]-alpha -Kdo-(2->6)-[lipid A] 3-alpha-heptosyltransferase"
source_database: "KEGG"
source_id: "R13004"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R13004"
---

# ADP-L-glycero-beta-D-manno-heptose:an alpha-L-glycero-D-manno-heptosyl-(1->5)-[alpha-Kdo-(2->4)]-alpha -Kdo-(2->6)-[lipid A] 3-alpha-heptosyltransferase

`reaction.R13004`

## Static

- Type: `reaction`
- Source: `KEGG:R13004`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADP-L-glycero-beta-D-manno-heptose + G06499 ADP + G13207

## Biological Role

Catalyzed by waaF (protein.P37692). Substrates: ADP-L-glycero-beta-D-manno-heptose (molecule.C06398). Products: ADP (molecule.C00008).

## Annotation

ADP-L-glycero-beta-D-manno-heptose + G06499 <=> ADP + G13207

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37692|protein.P37692]] `KEGG` `database` - via EC:2.4.99.24
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C06398 + G06499 <=> C00008 + G13207
- `is_substrate_of` <-- [[molecule.C06398|molecule.C06398]] `KEGG` `database` - C06398 + G06499 <=> C00008 + G13207

## External IDs

- `KEGG:R13004`

## Notes

EQUATION: C06398 + G06499 <=> C00008 + G13207
