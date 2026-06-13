---
entity_id: "molecule.C05172"
entity_type: "small_molecule"
name: "Selenophosphoric acid"
source_database: "KEGG"
source_id: "C05172"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Selenophosphoric acid"
  - "Selenophosphate"
---

# Selenophosphoric acid

`molecule.C05172`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05172`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Selenophosphoric acid; Selenophosphate EcoCyc common name: selenophosphate.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

KEGG compound: Selenophosphoric acid; Selenophosphate

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.2.7.9.3-RXN|reaction.ecocyc.2.7.9.3-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R08219|reaction.R08219]] `KEGG` `database` - C06481 + C05172 <=> C06482 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.2.9.1.1-RXN|reaction.ecocyc.2.9.1.1-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20756|reaction.ecocyc.RXN-20756]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2281|reaction.ecocyc.RXN0-2281]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05172`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
