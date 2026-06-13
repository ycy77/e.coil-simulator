---
entity_id: "molecule.C00098"
entity_type: "small_molecule"
name: "Oligopeptide"
source_database: "KEGG"
source_id: "C00098"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Oligopeptide"
---

# Oligopeptide

`molecule.C00098`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00098`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Oligopeptide EcoCyc common name: an oligopeptide.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Oligopeptide

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.3.6.3.23-RXN|reaction.ecocyc.3.6.3.23-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22655|reaction.ecocyc.RXN-22655]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7202|reaction.ecocyc.RXN0-7202]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3.4.21.83-RXN|reaction.ecocyc.3.4.21.83-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.3.4.24.70-RXN|reaction.ecocyc.3.4.24.70-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.3.6.3.23-RXN|reaction.ecocyc.3.6.3.23-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7202|reaction.ecocyc.RXN0-7202]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-41-CPLX|complex.ecocyc.ABC-41-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00098`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
