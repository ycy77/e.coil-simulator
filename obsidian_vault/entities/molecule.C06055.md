---
entity_id: "molecule.C06055"
entity_type: "small_molecule"
name: "O-Phospho-4-hydroxy-L-threonine"
source_database: "KEGG"
source_id: "C06055"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "O-Phospho-4-hydroxy-L-threonine"
  - "4-(Phosphonooxy)-threonine"
  - "4-(Phosphonooxy)-L-threonine"
  - "4-Phosphooxy-L-threonine"
---

# O-Phospho-4-hydroxy-L-threonine

`molecule.C06055`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06055`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: O-Phospho-4-hydroxy-L-threonine; 4-(Phosphonooxy)-threonine; 4-(Phosphonooxy)-L-threonine; 4-Phosphooxy-L-threonine EcoCyc common name: 4-phosphooxy-L-threonine.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: O-Phospho-4-hydroxy-L-threonine; 4-(Phosphonooxy)-threonine; 4-(Phosphonooxy)-L-threonine; 4-Phosphooxy-L-threonine

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN0-6564|reaction.ecocyc.RXN0-6564]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R05837|reaction.R05837]] `KEGG` `database` - C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.PSERTRANSAMPYR-RXN|reaction.ecocyc.PSERTRANSAMPYR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13179|reaction.ecocyc.RXN-13179]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.THRESYN-RXN|reaction.ecocyc.THRESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06055`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
