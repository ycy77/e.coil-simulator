---
entity_id: "molecule.C03196"
entity_type: "small_molecule"
name: "(S)-2-Hydroxyglutarate"
source_database: "KEGG"
source_id: "C03196"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-2-Hydroxyglutarate"
---

# (S)-2-Hydroxyglutarate

`molecule.C03196`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03196`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-2-Hydroxyglutarate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)

## Annotation

KEGG compound: (S)-2-Hydroxyglutarate

## Pathways

- `eco00310` Lysine degradation (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN0-7316|reaction.ecocyc.RXN0-7316]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16701|reaction.ecocyc.RXN-16701]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7319|reaction.ecocyc.RXN0-7319]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CHORISMATEMUT-RXN|reaction.ecocyc.CHORISMATEMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03196`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
