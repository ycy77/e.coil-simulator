---
entity_id: "molecule.C06508"
entity_type: "small_molecule"
name: "Adenosyl cobinamide"
source_database: "KEGG"
source_id: "C06508"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Adenosyl cobinamide"
  - "Adenosylcobinamide"
---

# Adenosyl cobinamide

`molecule.C06508`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06508`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Adenosyl cobinamide; Adenosylcobinamide EcoCyc common name: adenosylcobinamide.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Adenosyl cobinamide; Adenosylcobinamide

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R07268|reaction.R07268]] `KEGG` `database` - C00002 + C05774 <=> C00536 + C06508
- `is_product_of` --> [[reaction.ecocyc.BTUR2-RXN|reaction.ecocyc.BTUR2-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19343|reaction.ecocyc.RXN-19343]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.COBINAMIDEKIN-RXN|reaction.ecocyc.COBINAMIDEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06508`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
