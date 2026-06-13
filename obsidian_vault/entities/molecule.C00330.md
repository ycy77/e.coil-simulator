---
entity_id: "molecule.C00330"
entity_type: "small_molecule"
name: "Deoxyguanosine"
source_database: "KEGG"
source_id: "C00330"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Deoxyguanosine"
  - "2'-Deoxyguanosine"
---

# Deoxyguanosine

`molecule.C00330`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00330`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Deoxyguanosine; 2'-Deoxyguanosine EcoCyc common name: 2'-deoxyguanosine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Deoxyguanosine; 2'-Deoxyguanosine

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.DGTPTRIPHYDRO-RXN|reaction.ecocyc.DGTPTRIPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14142|reaction.ecocyc.RXN-14142]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14525|reaction.ecocyc.RXN-14525]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-475|reaction.ecocyc.TRANS-RXN-475]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN|reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-475|reaction.ecocyc.TRANS-RXN-475]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00330`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
