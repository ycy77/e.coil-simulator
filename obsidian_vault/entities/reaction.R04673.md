---
entity_id: "reaction.R04673"
entity_type: "reaction"
name: "(S)-2-aceto-2-hydroxybutanoate pyruvate-lyase (carboxylating)"
source_database: "KEGG"
source_id: "R04673"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04673"
---

# (S)-2-aceto-2-hydroxybutanoate pyruvate-lyase (carboxylating)

`reaction.R04673`

## Static

- Type: `reaction`
- Source: `KEGG:R04673`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Oxobutanoate + 2-(alpha-Hydroxyethyl)thiamine diphosphate (S)-2-Aceto-2-hydroxybutanoate + Thiamin diphosphate

## Biological Role

Catalyzed by ilvI (protein.P00893), ilvH (protein.P00894), ilvB (protein.P08142), ilvN (protein.P0ADF8), ilvM (protein.P0ADG1). Substrates: 2-Oxobutanoate (molecule.C00109), 2-(alpha-Hydroxyethyl)thiamine diphosphate (molecule.C05125). Products: Thiamin diphosphate (molecule.C00068), (S)-2-Aceto-2-hydroxybutanoate (molecule.C06006).

## Annotation

2-Oxobutanoate + 2-(alpha-Hydroxyethyl)thiamine diphosphate <=> (S)-2-Aceto-2-hydroxybutanoate + Thiamin diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P00893|protein.P00893]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P00894|protein.P00894]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P08142|protein.P08142]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P0ADF8|protein.P0ADF8]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P0ADG1|protein.P0ADG1]] `KEGG` `database` - via EC:2.2.1.6
- `is_product_of` <-- [[molecule.C00068|molecule.C00068]] `KEGG` `database` - C00109 + C05125 <=> C06006 + C00068
- `is_product_of` <-- [[molecule.C06006|molecule.C06006]] `KEGG` `database` - C00109 + C05125 <=> C06006 + C00068
- `is_substrate_of` <-- [[molecule.C00109|molecule.C00109]] `KEGG` `database` - C00109 + C05125 <=> C06006 + C00068
- `is_substrate_of` <-- [[molecule.C05125|molecule.C05125]] `KEGG` `database` - C00109 + C05125 <=> C06006 + C00068

## External IDs

- `KEGG:R04673`

## Notes

EQUATION: C00109 + C05125 <=> C06006 + C00068
