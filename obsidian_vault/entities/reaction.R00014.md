---
entity_id: "reaction.R00014"
entity_type: "reaction"
name: "pyruvate:thiamin diphosphate acetaldehydetransferase (decarboxylating)"
source_database: "KEGG"
source_id: "R00014"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00014"
---

# pyruvate:thiamin diphosphate acetaldehydetransferase (decarboxylating)

`reaction.R00014`

## Static

- Type: `reaction`
- Source: `KEGG:R00014`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyruvate + Thiamin diphosphate 2-(alpha-Hydroxyethyl)thiamine diphosphate + CO2

## Biological Role

Catalyzed by ilvI (protein.P00893), ilvH (protein.P00894), ilvB (protein.P08142), ilvN (protein.P0ADF8), ilvM (protein.P0ADG1), aceE (protein.P0AFG8). Substrates: Pyruvate (molecule.C00022), Thiamin diphosphate (molecule.C00068). Products: CO2 (molecule.C00011), 2-(alpha-Hydroxyethyl)thiamine diphosphate (molecule.C05125).

## Annotation

Pyruvate + Thiamin diphosphate <=> 2-(alpha-Hydroxyethyl)thiamine diphosphate + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P00893|protein.P00893]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P00894|protein.P00894]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P08142|protein.P08142]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P0ADF8|protein.P0ADF8]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P0ADG1|protein.P0ADG1]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P0AFG8|protein.P0AFG8]] `KEGG` `database` - via EC:1.2.4.1
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00022 + C00068 <=> C05125 + C00011
- `is_product_of` <-- [[molecule.C05125|molecule.C05125]] `KEGG` `database` - C00022 + C00068 <=> C05125 + C00011
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00022 + C00068 <=> C05125 + C00011
- `is_substrate_of` <-- [[molecule.C00068|molecule.C00068]] `KEGG` `database` - C00022 + C00068 <=> C05125 + C00011

## External IDs

- `KEGG:R00014`

## Notes

EQUATION: C00022 + C00068 <=> C05125 + C00011
