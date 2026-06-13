---
entity_id: "molecule.C00552"
entity_type: "small_molecule"
name: "meso-Tartaric acid"
source_database: "KEGG"
source_id: "C00552"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "meso-Tartaric acid"
  - "meso-Tartrate"
---

# meso-Tartaric acid

`molecule.C00552`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00552`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: meso-Tartaric acid; meso-Tartrate EcoCyc common name: meso-tartrate.

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: meso-Tartaric acid; meso-Tartrate

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7485|reaction.ecocyc.RXN0-7485]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.L-ASPARTATE-OXID-RXN|reaction.ecocyc.L-ASPARTATE-OXID-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LTARTDEHYDRA-RXN|reaction.ecocyc.LTARTDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00552`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
