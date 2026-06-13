---
entity_id: "molecule.C01151"
entity_type: "small_molecule"
name: "D-Ribose 1,5-bisphosphate"
source_database: "KEGG"
source_id: "C01151"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Ribose 1,5-bisphosphate"
  - "Ribose 1,5-bisphosphate"
  - "alpha-D-Ribose 1,5-bisphosphate"
---

# D-Ribose 1,5-bisphosphate

`molecule.C01151`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01151`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Ribose 1,5-bisphosphate; Ribose 1,5-bisphosphate; alpha-D-Ribose 1,5-bisphosphate EcoCyc common name: α-D-ribose 1,5-bisphosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)

## Annotation

KEGG compound: D-Ribose 1,5-bisphosphate; Ribose 1,5-bisphosphate; alpha-D-Ribose 1,5-bisphosphate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)

## Outgoing Edges (3)

- `activates` --> [[reaction.ecocyc.D-PPENTOMUT-RXN|reaction.ecocyc.D-PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.RXN0-6710|reaction.ecocyc.RXN0-6710]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1401|reaction.ecocyc.RXN0-1401]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01151`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
