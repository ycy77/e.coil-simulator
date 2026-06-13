---
entity_id: "molecule.C02188"
entity_type: "small_molecule"
name: "Protein lysine"
source_database: "KEGG"
source_id: "C02188"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Protein lysine"
  - "Peptidyl-L-lysine"
  - "[Protein]-L-lysine"
---

# Protein lysine

`molecule.C02188`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02188`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Protein lysine; Peptidyl-L-lysine; [Protein]-L-lysine EcoCyc common name: a [protein]-L-lysine.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)

## Annotation

KEGG compound: Protein lysine; Peptidyl-L-lysine; [Protein]-L-lysine

## Pathways

- `eco00310` Lysine degradation (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.3.4.19.12-RXN|reaction.ecocyc.3.4.19.12-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17632|reaction.ecocyc.RXN-17632]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19920|reaction.ecocyc.RXN-19920]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7078|reaction.ecocyc.RXN0-7078]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17631|reaction.ecocyc.RXN-17631]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25385|reaction.ecocyc.RXN-25385]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7160|reaction.ecocyc.RXN0-7160]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02188`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
