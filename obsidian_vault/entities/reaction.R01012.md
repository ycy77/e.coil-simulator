---
entity_id: "reaction.R01012"
entity_type: "reaction"
name: "phosphoenolpyruvate:glycerone phosphotransferase"
source_database: "KEGG"
source_id: "R01012"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01012"
---

# phosphoenolpyruvate:glycerone phosphotransferase

`reaction.R01012`

## Static

- Type: `reaction`
- Source: `KEGG:R01012`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Phosphoenolpyruvate + Glycerone Pyruvate + Glycerone phosphate

## Biological Role

Catalyzed by dhaM (protein.P37349), dhaL (protein.P76014), dhaK (protein.P76015). Substrates: Phosphoenolpyruvate (molecule.C00074), Glycerone (molecule.C00184). Products: Pyruvate (molecule.C00022), Glycerone phosphate (molecule.C00111).

## Annotation

Phosphoenolpyruvate + Glycerone <=> Pyruvate + Glycerone phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P37349|protein.P37349]] `KEGG` `database` - via EC:2.7.1.121
- `catalyzes` <-- [[protein.P76014|protein.P76014]] `KEGG` `database` - via EC:2.7.1.121
- `catalyzes` <-- [[protein.P76015|protein.P76015]] `KEGG` `database` - via EC:2.7.1.121
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00074 + C00184 <=> C00022 + C00111
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `KEGG` `database` - C00074 + C00184 <=> C00022 + C00111
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00074 + C00184 <=> C00022 + C00111
- `is_substrate_of` <-- [[molecule.C00184|molecule.C00184]] `KEGG` `database` - C00074 + C00184 <=> C00022 + C00111

## External IDs

- `KEGG:R01012`

## Notes

EQUATION: C00074 + C00184 <=> C00022 + C00111
