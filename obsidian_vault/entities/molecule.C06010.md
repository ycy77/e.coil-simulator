---
entity_id: "molecule.C06010"
entity_type: "small_molecule"
name: "(S)-2-Acetolactate"
source_database: "KEGG"
source_id: "C06010"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-2-Acetolactate"
  - "(S)-2-Hydroxy-2-methyl-3-oxobutanoate"
  - "(2S)-2-Hydroxy-2-methyl-3-oxobutanoate"
  - "(2S)-2-Hydroxy-2-methyl-3-oxobutanoic acid"
---

# (S)-2-Acetolactate

`molecule.C06010`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06010`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-2-Acetolactate; (S)-2-Hydroxy-2-methyl-3-oxobutanoate; (2S)-2-Hydroxy-2-methyl-3-oxobutanoate; (2S)-2-Hydroxy-2-methyl-3-oxobutanoic acid

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: (S)-2-Acetolactate; (S)-2-Hydroxy-2-methyl-3-oxobutanoate; (2S)-2-Hydroxy-2-methyl-3-oxobutanoate; (2S)-2-Hydroxy-2-methyl-3-oxobutanoic acid

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7715|complex.ecocyc.CPLX0-7715]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R04439|reaction.R04439]] `KEGG` `database` - C04272 + C00006 <=> C06010 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN|reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETOLACTSYN-RXN|reaction.ecocyc.ACETOLACTSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00226|reaction.R00226]] `KEGG` `database` - C06010 + C00011 <=> 2 C00022
- `is_substrate_of` --> [[reaction.R04672|reaction.R04672]] `KEGG` `database` - C06010 + C00068 <=> C05125 + C00022
- `is_substrate_of` --> [[reaction.ecocyc.RXN-6081|reaction.ecocyc.RXN-6081]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5392|reaction.ecocyc.RXN0-5392]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06010`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
