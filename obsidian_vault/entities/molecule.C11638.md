---
entity_id: "molecule.C11638"
entity_type: "small_molecule"
name: "3-Amino-2-oxopropyl phosphate"
source_database: "KEGG"
source_id: "C11638"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Amino-2-oxopropyl phosphate"
  - "1-Amino-3-(phosphohydroxy)propan-2-one"
---

# 3-Amino-2-oxopropyl phosphate

`molecule.C11638`

## Static

- Type: `small_molecule`
- Source: `KEGG:C11638`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Amino-2-oxopropyl phosphate; 1-Amino-3-(phosphohydroxy)propan-2-one EcoCyc common name: 3-amino-1-hydroxyacetone 1-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: 3-Amino-2-oxopropyl phosphate; 1-Amino-3-(phosphohydroxy)propan-2-one

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R05837|reaction.R05837]] `KEGG` `database` - C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011
- `is_product_of` --> [[reaction.ecocyc.RXN-13179|reaction.ecocyc.RXN-13179]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R05838|reaction.R05838]] `KEGG` `database` - C11638 + C11437 <=> C00627 + C00009 + 2 C00001
- `is_substrate_of` --> [[reaction.ecocyc.PDXJ-RXN|reaction.ecocyc.PDXJ-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C11638`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
