---
entity_id: "reaction.R00161"
entity_type: "reaction"
name: "ATP:FMN adenylyltransferase"
source_database: "KEGG"
source_id: "R00161"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00161"
---

# ATP:FMN adenylyltransferase

`reaction.R00161`

## Static

- Type: `reaction`
- Source: `KEGG:R00161`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + FMN Diphosphate + FAD

## Biological Role

Catalyzed by ribF (protein.P0AG40). Substrates: ATP (molecule.C00002), FMN (molecule.C00061). Products: Diphosphate (molecule.C00013), FAD (molecule.C00016).

## Annotation

ATP + FMN <=> Diphosphate + FAD

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AG40|protein.P0AG40]] `KEGG` `database` - via EC:2.7.7.2
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00061 <=> C00013 + C00016
- `is_product_of` <-- [[molecule.C00016|molecule.C00016]] `KEGG` `database` - C00002 + C00061 <=> C00013 + C00016
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00061 <=> C00013 + C00016
- `is_substrate_of` <-- [[molecule.C00061|molecule.C00061]] `KEGG` `database` - C00002 + C00061 <=> C00013 + C00016

## External IDs

- `KEGG:R00161`

## Notes

EQUATION: C00002 + C00061 <=> C00013 + C00016
