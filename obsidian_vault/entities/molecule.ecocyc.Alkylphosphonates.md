---
entity_id: "molecule.ecocyc.Alkylphosphonates"
entity_type: "small_molecule"
name: "an alkylphosphonate"
source_database: "EcoCyc"
source_id: "Alkylphosphonates"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "an alkylphosphate"
  - "alkylphosphonate"
  - "alkanephosphonate"
---

# an alkylphosphonate

`molecule.ecocyc.Alkylphosphonates`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Alkylphosphonates`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This compound class stands for generic and unspecified alkylphosphonate compounds. This compound class stands for generic and unspecified alkylphosphonate compounds.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

This compound class stands for generic and unspecified alkylphosphonate compounds.

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.ABC-23-RXN|reaction.ecocyc.ABC-23-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-23-RXN|reaction.ecocyc.ABC-23-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-23-CPLX|complex.ecocyc.ABC-23-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:Alkylphosphonates`
- `METANETX:MNXM8270`
- `CHEBI:60983`
