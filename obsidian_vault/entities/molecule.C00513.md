---
entity_id: "molecule.C00513"
entity_type: "small_molecule"
name: "CDP-glycerol"
source_database: "KEGG"
source_id: "C00513"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "CDP-glycerol"
  - "rac-CDP-glycerol"
---

# CDP-glycerol

`molecule.C00513`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00513`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: CDP-glycerol EcoCyc common name: (2R)-CDP-glycerol.

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: CDP-glycerol

## Pathways

- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (1)

- `is_substrate_of` --> [[reaction.ecocyc.RXN-18241|reaction.ecocyc.RXN-18241]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00513`
- `EcoCyc:CPD-26204`
- `CHEBI:17885`
- `canonicalized_from:molecule.ecocyc.CPD-26204`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-26204: EcoCyc:CPD-26204
