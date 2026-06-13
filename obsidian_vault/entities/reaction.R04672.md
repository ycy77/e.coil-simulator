---
entity_id: "reaction.R04672"
entity_type: "reaction"
name: "(S)-2-acetolactate pyruvate-lyase (carboxylating)"
source_database: "KEGG"
source_id: "R04672"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04672"
---

# (S)-2-acetolactate pyruvate-lyase (carboxylating)

`reaction.R04672`

## Static

- Type: `reaction`
- Source: `KEGG:R04672`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-2-Acetolactate + Thiamin diphosphate 2-(alpha-Hydroxyethyl)thiamine diphosphate + Pyruvate

## Biological Role

Catalyzed by ilvI (protein.P00893), ilvH (protein.P00894), ilvB (protein.P08142), ilvN (protein.P0ADF8), ilvM (protein.P0ADG1). Substrates: Thiamin diphosphate (molecule.C00068), (S)-2-Acetolactate (molecule.C06010). Products: Pyruvate (molecule.C00022), 2-(alpha-Hydroxyethyl)thiamine diphosphate (molecule.C05125).

## Annotation

(S)-2-Acetolactate + Thiamin diphosphate <=> 2-(alpha-Hydroxyethyl)thiamine diphosphate + Pyruvate

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P00893|protein.P00893]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P00894|protein.P00894]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P08142|protein.P08142]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P0ADF8|protein.P0ADF8]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P0ADG1|protein.P0ADG1]] `KEGG` `database` - via EC:2.2.1.6
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C06010 + C00068 <=> C05125 + C00022
- `is_product_of` <-- [[molecule.C05125|molecule.C05125]] `KEGG` `database` - C06010 + C00068 <=> C05125 + C00022
- `is_substrate_of` <-- [[molecule.C00068|molecule.C00068]] `KEGG` `database` - C06010 + C00068 <=> C05125 + C00022
- `is_substrate_of` <-- [[molecule.C06010|molecule.C06010]] `KEGG` `database` - C06010 + C00068 <=> C05125 + C00022

## External IDs

- `KEGG:R04672`

## Notes

EQUATION: C06010 + C00068 <=> C05125 + C00022
