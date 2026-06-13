---
entity_id: "molecule.C18096"
entity_type: "small_molecule"
name: "D-Allulose 6-phosphate"
source_database: "KEGG"
source_id: "C18096"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Allulose 6-phosphate"
---

# D-Allulose 6-phosphate

`molecule.C18096`

## Static

- Type: `small_molecule`
- Source: `KEGG:C18096`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Allulose 6-phosphate EcoCyc common name: D-psicose 6-phosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Annotation

KEGG compound: D-Allulose 6-phosphate

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R09030|reaction.R09030]] `KEGG` `database` - C02962 <=> C18096
- `is_product_of` --> [[reaction.ecocyc.RXN0-303|reaction.ecocyc.RXN0-303]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-304|reaction.ecocyc.RXN0-304]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C18096`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
