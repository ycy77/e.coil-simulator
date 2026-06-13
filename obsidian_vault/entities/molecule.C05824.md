---
entity_id: "molecule.C05824"
entity_type: "small_molecule"
name: "S-Sulfo-L-cysteine"
source_database: "KEGG"
source_id: "C05824"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "S-Sulfo-L-cysteine"
---

# S-Sulfo-L-cysteine

`molecule.C05824`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05824`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: S-Sulfo-L-cysteine

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Annotation

KEGG compound: S-Sulfo-L-cysteine

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R03132|reaction.R03132]] `KEGG` `database` - C00979 + C00320 <=> C05824 + C00033
- `is_product_of` --> [[reaction.ecocyc.SULFOCYS-RXN|reaction.ecocyc.SULFOCYS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-330|reaction.ecocyc.TRANS-RXN-330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18586|reaction.ecocyc.RXN-18586]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19629|reaction.ecocyc.RXN-19629]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-330|reaction.ecocyc.TRANS-RXN-330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P77529|protein.P77529]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C05824`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
