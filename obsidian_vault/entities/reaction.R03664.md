---
entity_id: "reaction.R03664"
entity_type: "reaction"
name: "L-tryptophan -tRNA(Trp) ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R03664"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03664"
---

# L-tryptophan -tRNA(Trp) ligase (AMP-forming)

`reaction.R03664`

## Static

- Type: `reaction`
- Source: `KEGG:R03664`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Tryptophan + tRNA(Trp) AMP + Diphosphate + L-Tryptophanyl-tRNA(Trp)

## Biological Role

Catalyzed by trpS (protein.P00954). Substrates: ATP (molecule.C00002), L-Tryptophan (molecule.C00078). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Tryptophanyl-tRNA(Trp) (molecule.C03512).

## Annotation

ATP + L-Tryptophan + tRNA(Trp) <=> AMP + Diphosphate + L-Tryptophanyl-tRNA(Trp)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00954|protein.P00954]] `KEGG` `database` - via EC:6.1.1.2
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00078 + C01652 <=> C00020 + C00013 + C03512
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00078 + C01652 <=> C00020 + C00013 + C03512
- `is_product_of` <-- [[molecule.C03512|molecule.C03512]] `KEGG` `database` - C00002 + C00078 + C01652 <=> C00020 + C00013 + C03512
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00078 + C01652 <=> C00020 + C00013 + C03512
- `is_substrate_of` <-- [[molecule.C00078|molecule.C00078]] `KEGG` `database` - C00002 + C00078 + C01652 <=> C00020 + C00013 + C03512

## External IDs

- `KEGG:R03664`

## Notes

EQUATION: C00002 + C00078 + C01652 <=> C00020 + C00013 + C03512
