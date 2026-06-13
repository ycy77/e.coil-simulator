---
entity_id: "reaction.R01900"
entity_type: "reaction"
name: "isocitrate hydro-lyase (cis-aconitate-forming)"
source_database: "KEGG"
source_id: "R01900"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01900"
---

# isocitrate hydro-lyase (cis-aconitate-forming)

`reaction.R01900`

## Static

- Type: `reaction`
- Source: `KEGG:R01900`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Isocitrate cis-Aconitate + H2O

## Biological Role

Catalyzed by acnA (protein.P25516), acnB (protein.P36683). Substrates: Isocitrate (molecule.C00311). Products: H2O (molecule.C00001), cis-Aconitate (molecule.C00417).

## Annotation

Isocitrate <=> cis-Aconitate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P25516|protein.P25516]] `KEGG` `database` - via EC:4.2.1.3
- `catalyzes` <-- [[protein.P36683|protein.P36683]] `KEGG` `database` - via EC:4.2.1.3
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00311 <=> C00417 + C00001
- `is_product_of` <-- [[molecule.C00417|molecule.C00417]] `KEGG` `database` - C00311 <=> C00417 + C00001
- `is_substrate_of` <-- [[molecule.C00311|molecule.C00311]] `KEGG` `database` - C00311 <=> C00417 + C00001

## External IDs

- `KEGG:R01900`

## Notes

EQUATION: C00311 <=> C00417 + C00001
