---
entity_id: "molecule.C05332"
entity_type: "small_molecule"
name: "Phenethylamine"
source_database: "KEGG"
source_id: "C05332"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phenethylamine"
  - "2-Phenylethylamine"
  - "beta-Phenylethylamine"
  - "Phenylethylamine"
---

# Phenethylamine

`molecule.C05332`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05332`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phenethylamine; 2-Phenylethylamine; beta-Phenylethylamine; Phenylethylamine EcoCyc common name: 2-phenylethylamine.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Annotation

KEGG compound: Phenethylamine; 2-Phenylethylamine; beta-Phenylethylamine; Phenylethylamine

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R02613|reaction.R02613]] `KEGG` `database` - C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10817|reaction.ecocyc.RXN-10817]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05332`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
