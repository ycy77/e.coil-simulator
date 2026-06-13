---
entity_id: "molecule.C00235"
entity_type: "small_molecule"
name: "Dimethylallyl diphosphate"
source_database: "KEGG"
source_id: "C00235"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dimethylallyl diphosphate"
  - "2-Isopentenyl diphosphate"
  - "Delta2-Isopentenyl diphosphate"
  - "Dimethylallyl pyrophosphate"
  - "DMAPP"
  - "Monoprenyl diphosphate"
  - "Prenyl diphosphate"
---

# Dimethylallyl diphosphate

`molecule.C00235`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00235`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dimethylallyl diphosphate; 2-Isopentenyl diphosphate; Delta2-Isopentenyl diphosphate; Dimethylallyl pyrophosphate; DMAPP; Monoprenyl diphosphate; Prenyl diphosphate EcoCyc common name: prenyl diphosphate.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Annotation

KEGG compound: Dimethylallyl diphosphate; 2-Isopentenyl diphosphate; Delta2-Isopentenyl diphosphate; Dimethylallyl pyrophosphate; DMAPP; Monoprenyl diphosphate; Prenyl diphosphate

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.IPPISOM-RXN|reaction.ecocyc.IPPISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R08210|reaction.R08210]] `KEGG` `database` - C00235 + 2 C00139 + C00001 <=> C11811 + 2 C00138 + 2 C00080
- `is_substrate_of` --> [[reaction.ecocyc.GPPSYN-RXN|reaction.ecocyc.GPPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24043|reaction.ecocyc.RXN-24043]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6274|reaction.ecocyc.RXN0-6274]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7309|reaction.ecocyc.RXN0-7309]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00235`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
