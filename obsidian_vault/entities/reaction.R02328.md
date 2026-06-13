---
entity_id: "reaction.R02328"
entity_type: "reaction"
name: "dTTP:alpha-D-glucose-1-phosphate thymidylyltransferase"
source_database: "KEGG"
source_id: "R02328"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02328"
---

# dTTP:alpha-D-glucose-1-phosphate thymidylyltransferase

`reaction.R02328`

## Static

- Type: `reaction`
- Source: `KEGG:R02328`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

dTTP + D-Glucose 1-phosphate Diphosphate + dTDP-glucose

## Biological Role

Catalyzed by rfbA (protein.P37744), rffH (protein.P61887). Substrates: D-Glucose 1-phosphate (molecule.C00103), dTTP (molecule.C00459). Products: Diphosphate (molecule.C00013), dTDP-glucose (molecule.C00842).

## Annotation

dTTP + D-Glucose 1-phosphate <=> Diphosphate + dTDP-glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37744|protein.P37744]] `KEGG` `database` - via EC:2.7.7.24
- `catalyzes` <-- [[protein.P61887|protein.P61887]] `KEGG` `database` - via EC:2.7.7.24
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00459 + C00103 <=> C00013 + C00842
- `is_product_of` <-- [[molecule.C00842|molecule.C00842]] `KEGG` `database` - C00459 + C00103 <=> C00013 + C00842
- `is_substrate_of` <-- [[molecule.C00103|molecule.C00103]] `KEGG` `database` - C00459 + C00103 <=> C00013 + C00842
- `is_substrate_of` <-- [[molecule.C00459|molecule.C00459]] `KEGG` `database` - C00459 + C00103 <=> C00013 + C00842

## External IDs

- `KEGG:R02328`

## Notes

EQUATION: C00459 + C00103 <=> C00013 + C00842
