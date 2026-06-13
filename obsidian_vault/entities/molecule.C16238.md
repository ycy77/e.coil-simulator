---
entity_id: "molecule.C16238"
entity_type: "small_molecule"
name: "Lipoyl-AMP"
source_database: "KEGG"
source_id: "C16238"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Lipoyl-AMP"
---

# Lipoyl-AMP

`molecule.C16238`

## Static

- Type: `small_molecule`
- Source: `KEGG:C16238`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Lipoyl-AMP EcoCyc common name: [(R)-lipoyl]adenylate.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: Lipoyl-AMP

## Pathways

- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R07770|reaction.R07770]] `KEGG` `database` - C00002 + C16241 <=> C00013 + C16238
- `is_product_of` --> [[reaction.ecocyc.RXN-8654|reaction.ecocyc.RXN-8654]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R07771|reaction.R07771]] `KEGG` `database` - C16238 + C16240 <=> C16237 + C00020
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13039|reaction.ecocyc.RXN-13039]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8655|reaction.ecocyc.RXN-8655]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7424|reaction.ecocyc.RXN0-7424]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7425|reaction.ecocyc.RXN0-7425]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C16238`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
