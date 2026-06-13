---
entity_id: "molecule.C06398"
entity_type: "small_molecule"
name: "ADP-L-glycero-beta-D-manno-heptose"
source_database: "KEGG"
source_id: "C06398"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "ADP-L-glycero-beta-D-manno-heptose"
---

# ADP-L-glycero-beta-D-manno-heptose

`molecule.C06398`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06398`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: ADP-L-glycero-beta-D-manno-heptose EcoCyc common name: ADP-L-glycero-β-D-manno-heptose.

## Biological Role

Consumed as substrate in 9 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: ADP-L-glycero-beta-D-manno-heptose

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.ecocyc.5.1.3.20-RXN|reaction.ecocyc.5.1.3.20-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R13003|reaction.R13003]] `KEGG` `database` - C06398 + G00651 <=> C00008 + G06499
- `is_substrate_of` --> [[reaction.R13004|reaction.R13004]] `KEGG` `database` - C06398 + G06499 <=> C00008 + G13207
- `is_substrate_of` --> [[reaction.R13005|reaction.R13005]] `KEGG` `database` - C06398 + G13208 <=> C00008 + G13209
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22462|reaction.ecocyc.RXN-22462]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5057|reaction.ecocyc.RXN0-5057]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5061|reaction.ecocyc.RXN0-5061]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5118|reaction.ecocyc.RXN0-5118]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5122|reaction.ecocyc.RXN0-5122]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5127|reaction.ecocyc.RXN0-5127]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06398`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
