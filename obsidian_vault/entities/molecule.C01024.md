---
entity_id: "molecule.C01024"
entity_type: "small_molecule"
name: "Hydroxymethylbilane"
source_database: "KEGG"
source_id: "C01024"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Hydroxymethylbilane"
---

# Hydroxymethylbilane

`molecule.C01024`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01024`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Hydroxymethylbilane EcoCyc common name: preuroporphyrinogen.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Hydroxymethylbilane

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R00084|reaction.R00084]] `KEGG` `database` - 4 C00931 + C00001 <=> C01024 + 4 C00014
- `is_product_of` --> [[reaction.ecocyc.OHMETHYLBILANESYN-RXN|reaction.ecocyc.OHMETHYLBILANESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21525|reaction.ecocyc.RXN-21525]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03165|reaction.R03165]] `KEGG` `database` - C01024 <=> C01051 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14396|reaction.ecocyc.RXN-14396]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UROGENIIISYN-RXN|reaction.ecocyc.UROGENIIISYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01024`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
