---
entity_id: "reaction.R02601"
entity_type: "reaction"
name: "4-hydroxy-2-oxopentanoate hydro-lyase (2-oxopent-4-enoate-forming)"
source_database: "KEGG"
source_id: "R02601"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02601"
---

# 4-hydroxy-2-oxopentanoate hydro-lyase (2-oxopent-4-enoate-forming)

`reaction.R02601`

## Static

- Type: `reaction`
- Source: `KEGG:R02601`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Hydroxy-2,4-pentadienoate + H2O 4-Hydroxy-2-oxopentanoate

## Biological Role

Catalyzed by mhpD (protein.P77608). Substrates: H2O (molecule.C00001), 2-Hydroxy-2,4-pentadienoate (molecule.C00596). Products: 4-Hydroxy-2-oxopentanoate (molecule.C03589).

## Annotation

2-Hydroxy-2,4-pentadienoate + H2O <=> 4-Hydroxy-2-oxopentanoate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77608|protein.P77608]] `KEGG` `database` - via EC:4.2.1.80
- `is_product_of` <-- [[molecule.C03589|molecule.C03589]] `KEGG` `database` - C00596 + C00001 <=> C03589
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00596 + C00001 <=> C03589
- `is_substrate_of` <-- [[molecule.C00596|molecule.C00596]] `KEGG` `database` - C00596 + C00001 <=> C03589

## External IDs

- `KEGG:R02601`

## Notes

EQUATION: C00596 + C00001 <=> C03589
