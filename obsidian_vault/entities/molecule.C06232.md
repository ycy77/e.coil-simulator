---
entity_id: "molecule.C06232"
entity_type: "small_molecule"
name: "Molybdate"
source_database: "KEGG"
source_id: "C06232"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Molybdate"
---

# Molybdate

`molecule.C06232`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06232`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Molybdate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Molybdate

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (7)

- `is_component_of` --> [[complex.ecocyc.CPLX0-6|complex.ecocyc.CPLX0-6]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.ABC-19-RXN|reaction.ecocyc.ABC-19-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-19-RXN|reaction.ecocyc.ABC-19-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21563|reaction.ecocyc.RXN-21563]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24141|reaction.ecocyc.RXN-24141]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7|reaction.ecocyc.RXN0-7]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ALKAPHOSPHA-RXN|reaction.ecocyc.ALKAPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-7-CPLX|complex.ecocyc.ABC-7-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C06232`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
