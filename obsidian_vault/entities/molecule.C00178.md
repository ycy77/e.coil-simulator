---
entity_id: "molecule.C00178"
entity_type: "small_molecule"
name: "Thymine"
source_database: "KEGG"
source_id: "C00178"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Thymine"
  - "5-Methyluracil"
---

# Thymine

`molecule.C00178`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00178`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Thymine; 5-Methyluracil

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: Thymine; 5-Methyluracil

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (12)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8058|complex.ecocyc.CPLX0-8058]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN0-6565|reaction.ecocyc.RXN0-6565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THYM-PHOSPH-RXN|reaction.ecocyc.THYM-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-362|reaction.ecocyc.TRANS-RXN-362]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-524|reaction.ecocyc.TRANS-RXN0-524]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12886|reaction.ecocyc.RXN-12886]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20708|reaction.ecocyc.RXN-20708]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6468|reaction.ecocyc.RXN0-6468]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-362|reaction.ecocyc.TRANS-RXN-362]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-524|reaction.ecocyc.TRANS-RXN0-524]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.THYM-PHOSPH-RXN|reaction.ecocyc.THYM-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN-132|reaction.ecocyc.TRANS-RXN-132]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P75892|protein.P75892]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00178`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
