---
entity_id: "molecule.C00502"
entity_type: "small_molecule"
name: "D-Xylonate"
source_database: "KEGG"
source_id: "C00502"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Xylonate"
---

# D-Xylonate

`molecule.C00502`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00502`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Xylonate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: D-Xylonate

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (7)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8257|complex.ecocyc.CPLX0-8257]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN-12246|reaction.ecocyc.RXN-12246]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19753|reaction.ecocyc.RXN-19753]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-361|reaction.ecocyc.TRANS-RXN-361]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7287|reaction.ecocyc.RXN0-7287]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-361|reaction.ecocyc.TRANS-RXN-361]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN|reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00502`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
