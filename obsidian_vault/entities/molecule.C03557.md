---
entity_id: "molecule.C03557"
entity_type: "small_molecule"
name: "2-Aminoethylphosphonate"
source_database: "KEGG"
source_id: "C03557"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Aminoethylphosphonate"
  - "(2-Aminoethyl)phosphonate"
  - "Ciliatine"
---

# 2-Aminoethylphosphonate

`molecule.C03557`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03557`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Aminoethylphosphonate; (2-Aminoethyl)phosphonate; Ciliatine EcoCyc common name: (2-aminoethyl)phosphonate.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: 2-Aminoethylphosphonate; (2-Aminoethyl)phosphonate; Ciliatine

## Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R11479|reaction.R11479]] `KEGG` `database` - C00024 + C03557 <=> C21403 + C00010
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17962|reaction.ecocyc.RXN-17962]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03557`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
