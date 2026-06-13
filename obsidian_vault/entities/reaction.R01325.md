---
entity_id: "reaction.R01325"
entity_type: "reaction"
name: "citrate hydro-lyase (cis-aconitate-forming)"
source_database: "KEGG"
source_id: "R01325"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01325"
---

# citrate hydro-lyase (cis-aconitate-forming)

`reaction.R01325`

## Static

- Type: `reaction`
- Source: `KEGG:R01325`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Citrate cis-Aconitate + H2O

## Biological Role

Catalyzed by acnA (protein.P25516), acnB (protein.P36683). Substrates: Citrate (molecule.C00158). Products: H2O (molecule.C00001), cis-Aconitate (molecule.C00417).

## Annotation

Citrate <=> cis-Aconitate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P25516|protein.P25516]] `KEGG` `database` - via EC:4.2.1.3
- `catalyzes` <-- [[protein.P36683|protein.P36683]] `KEGG` `database` - via EC:4.2.1.3
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00158 <=> C00417 + C00001
- `is_product_of` <-- [[molecule.C00417|molecule.C00417]] `KEGG` `database` - C00158 <=> C00417 + C00001
- `is_substrate_of` <-- [[molecule.C00158|molecule.C00158]] `KEGG` `database` - C00158 <=> C00417 + C00001

## External IDs

- `KEGG:R01325`

## Notes

EQUATION: C00158 <=> C00417 + C00001
