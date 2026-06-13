---
entity_id: "molecule.C00596"
entity_type: "small_molecule"
name: "2-Hydroxy-2,4-pentadienoate"
source_database: "KEGG"
source_id: "C00596"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Hydroxy-2,4-pentadienoate"
  - "cis-2-Hydroxypenta-2,4-dienoate"
  - "Oxopent-4-enoate"
  - "2-Oxopent-4-enoate"
  - "2-Hydroxypenta-2,4-dienoate"
---

# 2-Hydroxy-2,4-pentadienoate

`molecule.C00596`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00596`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Hydroxy-2,4-pentadienoate; cis-2-Hydroxypenta-2,4-dienoate; Oxopent-4-enoate; 2-Oxopent-4-enoate; 2-Hydroxypenta-2,4-dienoate EcoCyc common name: 2-oxopent-4-enoate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)

## Annotation

KEGG compound: 2-Hydroxy-2,4-pentadienoate; cis-2-Hydroxypenta-2,4-dienoate; Oxopent-4-enoate; 2-Oxopent-4-enoate; 2-Hydroxypenta-2,4-dienoate

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN-19492|reaction.ecocyc.RXN-19492]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02601|reaction.R02601]] `KEGG` `database` - C00596 + C00001 <=> C03589
- `is_substrate_of` --> [[reaction.R02603|reaction.R02603]] `KEGG` `database` - C00596 + C00042 <=> C04479 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.RXN-7282|reaction.ecocyc.RXN-7282]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00596`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
