---
entity_id: "molecule.C05921"
entity_type: "small_molecule"
name: "Biotinyl-5'-AMP"
source_database: "KEGG"
source_id: "C05921"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Biotinyl-5'-AMP"
---

# Biotinyl-5'-AMP

`molecule.C05921`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05921`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Biotinyl-5'-AMP EcoCyc common name: biotinyl-5'-adenylate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)

## Annotation

KEGG compound: Biotinyl-5'-AMP

## Pathways

- `eco00780` Biotin metabolism (KEGG)

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.MONOMER-48|complex.ecocyc.MONOMER-48]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN0-7192|reaction.ecocyc.RXN0-7192]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.R131-RXN|reaction.ecocyc.R131-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22002|reaction.ecocyc.RXN-22002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05921`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
