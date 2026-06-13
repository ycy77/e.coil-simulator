---
entity_id: "molecule.C06696"
entity_type: "small_molecule"
name: "Lead"
source_database: "KEGG"
source_id: "C06696"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Lead"
  - "Pb"
---

# Lead

`molecule.C06696`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06696`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Lead; Pb EcoCyc common name: Pb2+.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Lead; Pb

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-452|reaction.ecocyc.TRANS-RXN-452]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-452|reaction.ecocyc.TRANS-RXN-452]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P37617|protein.P37617]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C06696`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
