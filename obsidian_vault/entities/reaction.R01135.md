---
entity_id: "reaction.R01135"
entity_type: "reaction"
name: "IMP:L-aspartate ligase (GDP-forming)"
source_database: "KEGG"
source_id: "R01135"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01135"
---

# IMP:L-aspartate ligase (GDP-forming)

`reaction.R01135`

## Static

- Type: `reaction`
- Source: `KEGG:R01135`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + IMP + L-Aspartate GDP + Orthophosphate + N6-(1,2-Dicarboxyethyl)-AMP

## Biological Role

Catalyzed by purA (protein.P0A7D4). Substrates: GTP (molecule.C00044), L-Aspartate (molecule.C00049), IMP (molecule.C00130). Products: Orthophosphate (molecule.C00009), GDP (molecule.C00035), N6-(1,2-Dicarboxyethyl)-AMP (molecule.C03794).

## Annotation

GTP + IMP + L-Aspartate <=> GDP + Orthophosphate + N6-(1,2-Dicarboxyethyl)-AMP

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A7D4|protein.P0A7D4]] `KEGG` `database` - via EC:6.3.4.4
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_product_of` <-- [[molecule.C03794|molecule.C03794]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_substrate_of` <-- [[molecule.C00130|molecule.C00130]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794

## External IDs

- `KEGG:R01135`

## Notes

EQUATION: C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
