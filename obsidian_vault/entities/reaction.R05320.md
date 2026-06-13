---
entity_id: "reaction.R05320"
entity_type: "reaction"
name: "taurine,2-oxoglutarate:O2 oxidoreductase (sulfite-forming)"
source_database: "KEGG"
source_id: "R05320"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05320"
---

# taurine,2-oxoglutarate:O2 oxidoreductase (sulfite-forming)

`reaction.R05320`

## Static

- Type: `reaction`
- Source: `KEGG:R05320`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Taurine + 2-Oxoglutarate + Oxygen Sulfite + Aminoacetaldehyde + Succinate + CO2

## Biological Role

Catalyzed by tauD (protein.P37610). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), Taurine (molecule.C00245). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), Sulfite (molecule.C00094), Aminoacetaldehyde (molecule.C06735).

## Annotation

Taurine + 2-Oxoglutarate + Oxygen <=> Sulfite + Aminoacetaldehyde + Succinate + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P37610|protein.P37610]] `KEGG` `database` - via EC:1.14.11.17
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_product_of` <-- [[molecule.C06735|molecule.C06735]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_substrate_of` <-- [[molecule.C00245|molecule.C00245]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011

## External IDs

- `KEGG:R05320`

## Notes

EQUATION: C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
