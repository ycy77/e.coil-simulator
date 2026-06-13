---
entity_id: "molecule.C00257"
entity_type: "small_molecule"
name: "D-Gluconic acid"
source_database: "KEGG"
source_id: "C00257"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Gluconic acid"
  - "D-Gluconate"
  - "D-gluco-Hexonic acid"
---

# D-Gluconic acid

`molecule.C00257`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00257`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Gluconic acid; D-Gluconate; D-gluco-Hexonic acid EcoCyc common name: D-gluconate.

## Biological Role

Consumed as substrate in 10 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Annotation

KEGG compound: D-Gluconic acid; D-Gluconate; D-gluco-Hexonic acid

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Outgoing Edges (16)

- `is_component_of` --> [[complex.ecocyc.MONOMER-55|complex.ecocyc.MONOMER-55]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.GLUCONOLACT-RXN|reaction.ecocyc.GLUCONOLACT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17754|reaction.ecocyc.RXN-17754]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5185|reaction.ecocyc.RXN0-5185]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-209|reaction.ecocyc.TRANS-RXN0-209]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01737|reaction.R01737]] `KEGG` `database` - C00002 + C00257 <=> C00008 + C00345
- `is_substrate_of` --> [[reaction.R01738|reaction.R01738]] `KEGG` `database` - C00257 + C00003 <=> C01062 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R01739|reaction.R01739]] `KEGG` `database` - C00257 + C00006 <=> C06473 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R01740|reaction.R01740]] `KEGG` `database` - C00257 + C00006 <=> C01062 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.215-RXN|reaction.ecocyc.1.1.1.215-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUCONATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.GLUCONATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUCONOKIN-RXN|reaction.ecocyc.GLUCONOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R143-RXN|reaction.ecocyc.R143-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7101|reaction.ecocyc.RXN0-7101]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-209|reaction.ecocyc.TRANS-RXN0-209]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AC94|protein.P0AC94]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00257`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
