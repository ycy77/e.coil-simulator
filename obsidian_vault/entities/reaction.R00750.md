---
entity_id: "reaction.R00750"
entity_type: "reaction"
name: "4-hydroxy-2-oxopentanoate pyruvate-lyase (acetaldehyde-forming)"
source_database: "KEGG"
source_id: "R00750"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00750"
---

# 4-hydroxy-2-oxopentanoate pyruvate-lyase (acetaldehyde-forming)

`reaction.R00750`

## Static

- Type: `reaction`
- Source: `KEGG:R00750`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetaldehyde + Pyruvate 4-Hydroxy-2-oxopentanoate

## Biological Role

Catalyzed by mhpE (protein.P51020). Substrates: Pyruvate (molecule.C00022), Acetaldehyde (molecule.C00084). Products: 4-Hydroxy-2-oxopentanoate (molecule.C03589).

## Annotation

Acetaldehyde + Pyruvate <=> 4-Hydroxy-2-oxopentanoate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P51020|protein.P51020]] `KEGG` `database` - via EC:4.1.3.39
- `is_product_of` <-- [[molecule.C03589|molecule.C03589]] `KEGG` `database` - C00084 + C00022 <=> C03589
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00084 + C00022 <=> C03589
- `is_substrate_of` <-- [[molecule.C00084|molecule.C00084]] `KEGG` `database` - C00084 + C00022 <=> C03589

## External IDs

- `KEGG:R00750`

## Notes

EQUATION: C00084 + C00022 <=> C03589
