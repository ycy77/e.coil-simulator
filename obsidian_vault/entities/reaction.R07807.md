---
entity_id: "reaction.R07807"
entity_type: "reaction"
name: "R07807"
source_database: "KEGG"
source_id: "R07807"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07807"
---

# R07807

`reaction.R07807`

## Static

- Type: `reaction`
- Source: `KEGG:R07807`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

G01977 + H2O G13073 + D-Galactose

## Biological Role

Catalyzed by lacZ (protein.P00722), ebgA (protein.P06864). Substrates: H2O (molecule.C00001). Products: D-Galactose (molecule.C00124).

## Annotation

G01977 + H2O <=> G13073 + D-Galactose

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P00722|protein.P00722]] `KEGG` `database` - via EC:3.2.1.23
- `catalyzes` <-- [[protein.P06864|protein.P06864]] `KEGG` `database` - via EC:3.2.1.23
- `is_product_of` <-- [[molecule.C00124|molecule.C00124]] `KEGG` `database` - G01977 + C00001 <=> G13073 + C00124
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - G01977 + C00001 <=> G13073 + C00124

## External IDs

- `KEGG:R07807`

## Notes

EQUATION: G01977 + C00001 <=> G13073 + C00124
