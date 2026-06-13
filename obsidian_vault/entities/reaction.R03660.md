---
entity_id: "reaction.R03660"
entity_type: "reaction"
name: "L-phenylalanine:tRNA(Ala) ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R03660"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03660"
---

# L-phenylalanine:tRNA(Ala) ligase (AMP-forming)

`reaction.R03660`

## Static

- Type: `reaction`
- Source: `KEGG:R03660`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Phenylalanine + tRNA(Phe) AMP + Diphosphate + L-Phenylalanyl-tRNA(Phe)

## Biological Role

Catalyzed by pheT (protein.P07395), pheS (protein.P08312). Substrates: ATP (molecule.C00002), L-Phenylalanine (molecule.C00079). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Phenylalanyl-tRNA(Phe) (molecule.C03511).

## Annotation

ATP + L-Phenylalanine + tRNA(Phe) <=> AMP + Diphosphate + L-Phenylalanyl-tRNA(Phe)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P07395|protein.P07395]] `KEGG` `database` - via EC:6.1.1.20
- `catalyzes` <-- [[protein.P08312|protein.P08312]] `KEGG` `database` - via EC:6.1.1.20
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00079 + C01648 <=> C00020 + C00013 + C03511
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00079 + C01648 <=> C00020 + C00013 + C03511
- `is_product_of` <-- [[molecule.C03511|molecule.C03511]] `KEGG` `database` - C00002 + C00079 + C01648 <=> C00020 + C00013 + C03511
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00079 + C01648 <=> C00020 + C00013 + C03511
- `is_substrate_of` <-- [[molecule.C00079|molecule.C00079]] `KEGG` `database` - C00002 + C00079 + C01648 <=> C00020 + C00013 + C03511

## External IDs

- `KEGG:R03660`

## Notes

EQUATION: C00002 + C00079 + C01648 <=> C00020 + C00013 + C03511
