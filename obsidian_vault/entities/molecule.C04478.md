---
entity_id: "molecule.C04478"
entity_type: "small_molecule"
name: "3-Deoxy-D-manno-octulosonate 8-phosphate"
source_database: "KEGG"
source_id: "C04478"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Deoxy-D-manno-octulosonate 8-phosphate"
  - "2-Dehydro-3-deoxy-D-octonate 8-phosphate"
---

# 3-Deoxy-D-manno-octulosonate 8-phosphate

`molecule.C04478`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04478`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Deoxy-D-manno-octulosonate 8-phosphate; 2-Dehydro-3-deoxy-D-octonate 8-phosphate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: 3-Deoxy-D-manno-octulosonate 8-phosphate; 2-Dehydro-3-deoxy-D-octonate 8-phosphate

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.KDO-8PSYNTH-RXN|reaction.ecocyc.KDO-8PSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.KDO-8PPHOSPHAT-RXN|reaction.ecocyc.KDO-8PPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDO-8PSYNTH-RXN|reaction.ecocyc.KDO-8PSYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04478`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
