---
entity_id: "molecule.C02989"
entity_type: "small_molecule"
name: "L-Methionine S-oxide"
source_database: "KEGG"
source_id: "C02989"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Methionine S-oxide"
---

# L-Methionine S-oxide

`molecule.C02989`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02989`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Methionine S-oxide

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Annotation

KEGG compound: L-Methionine S-oxide

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN0-6721|reaction.ecocyc.RXN0-6721]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-511|reaction.ecocyc.TRANS-RXN0-511]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-511|reaction.ecocyc.TRANS-RXN0-511]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX|complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C02989`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
