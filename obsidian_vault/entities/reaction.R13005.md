---
entity_id: "reaction.R13005"
entity_type: "reaction"
name: "ADP-L-glycero-beta-D-manno-heptose:an alpha-Hep-(1->3)-4-O-phospho-alpha-Hep-(1->5)-[alpha-Kdo-(2->4)]-alpha-Kdo-(2->6)-[lipid A] heptoseI 7-alpha-heptosyltransferase"
source_database: "KEGG"
source_id: "R13005"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R13005"
---

# ADP-L-glycero-beta-D-manno-heptose:an alpha-Hep-(1->3)-4-O-phospho-alpha-Hep-(1->5)-[alpha-Kdo-(2->4)]-alpha-Kdo-(2->6)-[lipid A] heptoseI 7-alpha-heptosyltransferase

`reaction.R13005`

## Static

- Type: `reaction`
- Source: `KEGG:R13005`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADP-L-glycero-beta-D-manno-heptose + G13208 ADP + G13209

## Biological Role

Catalyzed by waaQ (protein.P25742). Substrates: ADP-L-glycero-beta-D-manno-heptose (molecule.C06398). Products: ADP (molecule.C00008).

## Annotation

ADP-L-glycero-beta-D-manno-heptose + G13208 <=> ADP + G13209

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P25742|protein.P25742]] `KEGG` `database` - via EC:2.4.99.25
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C06398 + G13208 <=> C00008 + G13209
- `is_substrate_of` <-- [[molecule.C06398|molecule.C06398]] `KEGG` `database` - C06398 + G13208 <=> C00008 + G13209

## External IDs

- `KEGG:R13005`

## Notes

EQUATION: C06398 + G13208 <=> C00008 + G13209
