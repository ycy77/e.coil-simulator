---
entity_id: "molecule.C00325"
entity_type: "small_molecule"
name: "GDP-L-fucose"
source_database: "KEGG"
source_id: "C00325"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "GDP-L-fucose"
  - "GDP-beta-L-fucose"
---

# GDP-L-fucose

`molecule.C00325`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00325`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: GDP-L-fucose; GDP-beta-L-fucose EcoCyc common name: GDP-β-L-fucose.

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: GDP-L-fucose; GDP-beta-L-fucose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (6)

- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.271-RXN|reaction.ecocyc.1.1.1.271-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FCLREDUCT-RXN|reaction.ecocyc.FCLREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7341|reaction.ecocyc.RXN0-7341]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7343|reaction.ecocyc.RXN0-7343]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.1.1.271-RXN|reaction.ecocyc.1.1.1.271-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GDPMANDEHYDRA-RXN|reaction.ecocyc.GDPMANDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00325`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
