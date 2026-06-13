---
entity_id: "molecule.ecocyc.Unspecified-Ion-Or-Solute"
entity_type: "small_molecule"
name: "non-specific ion/solute"
source_database: "EcoCyc"
source_id: "Unspecified-Ion-Or-Solute"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# non-specific ion/solute

`molecule.ecocyc.Unspecified-Ion-Or-Solute`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Unspecified-Ion-Or-Solute`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This compound class stands for generic and unspecified ions or solutes in transport reactions. Once a given transporter is better characterized, a more specific compound class should be substituted instead. This compound class stands for generic and unspecified ions or solutes in transport reactions. Once a given transporter is better characterized, a more specific compound class should be substituted instead.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Annotation

This compound class stands for generic and unspecified ions or solutes in transport reactions. Once a given transporter is better characterized, a more specific compound class should be substituted instead.

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN0-1804|reaction.ecocyc.RXN0-1804]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-86|reaction.ecocyc.TRANS-RXN-86]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1804|reaction.ecocyc.RXN0-1804]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-86|reaction.ecocyc.TRANS-RXN-86]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Unspecified-Ion-Or-Solute`
