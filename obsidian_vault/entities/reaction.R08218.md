---
entity_id: "reaction.R08218"
entity_type: "reaction"
name: "L-serine:tRNASec ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R08218"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08218"
---

# L-serine:tRNASec ligase (AMP-forming)

`reaction.R08218`

## Static

- Type: `reaction`
- Source: `KEGG:R08218`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Serine + tRNA(Sec) AMP + Diphosphate + L-Seryl-tRNA(Sec)

## Biological Role

Catalyzed by serS (protein.P0A8L1). Substrates: ATP (molecule.C00002), L-Serine (molecule.C00065). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Seryl-tRNA(Sec) (molecule.C06481).

## Annotation

ATP + L-Serine + tRNA(Sec) <=> AMP + Diphosphate + L-Seryl-tRNA(Sec)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A8L1|protein.P0A8L1]] `KEGG` `database` - via EC:6.1.1.11
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00065 + C16636 <=> C00020 + C00013 + C06481
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00065 + C16636 <=> C00020 + C00013 + C06481
- `is_product_of` <-- [[molecule.C06481|molecule.C06481]] `KEGG` `database` - C00002 + C00065 + C16636 <=> C00020 + C00013 + C06481
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00065 + C16636 <=> C00020 + C00013 + C06481
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `KEGG` `database` - C00002 + C00065 + C16636 <=> C00020 + C00013 + C06481

## External IDs

- `KEGG:R08218`

## Notes

EQUATION: C00002 + C00065 + C16636 <=> C00020 + C00013 + C06481
