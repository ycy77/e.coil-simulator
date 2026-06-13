---
entity_id: "reaction.R02624"
entity_type: "reaction"
name: "protein-L-glutamate-O4-methyl-ester acylhydrolase"
source_database: "KEGG"
source_id: "R02624"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02624"
---

# protein-L-glutamate-O4-methyl-ester acylhydrolase

`reaction.R02624`

## Static

- Type: `reaction`
- Source: `KEGG:R02624`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein glutamate methyl ester + H2O Protein glutamate + Methanol

## Biological Role

Catalyzed by cheB (protein.P07330). Substrates: H2O (molecule.C00001). Products: Methanol (molecule.C00132).

## Annotation

Protein glutamate methyl ester + H2O <=> Protein glutamate + Methanol

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07330|protein.P07330]] `KEGG` `database` - via EC:3.1.1.61
- `is_product_of` <-- [[molecule.C00132|molecule.C00132]] `KEGG` `database` - C04142 + C00001 <=> C00614 + C00132
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04142 + C00001 <=> C00614 + C00132

## External IDs

- `KEGG:R02624`

## Notes

EQUATION: C04142 + C00001 <=> C00614 + C00132
