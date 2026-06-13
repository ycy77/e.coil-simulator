---
entity_id: "molecule.C00116"
entity_type: "small_molecule"
name: "Glycerol"
source_database: "KEGG"
source_id: "C00116"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glycerol"
  - "Glycerin"
  - "1,2,3-Trihydroxypropane"
  - "1,2,3-Propanetriol"
---

# Glycerol

`molecule.C00116`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00116`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glycerol; Glycerin; 1,2,3-Trihydroxypropane; 1,2,3-Propanetriol

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Glycerol; Glycerin; 1,2,3-Trihydroxypropane; 1,2,3-Propanetriol

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (16)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8057|complex.ecocyc.CPLX0-8057]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.CARDIOLIPSYN-RXN|reaction.ecocyc.CARDIOLIPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYCEROL-1-PHOSPHATASE-RXN|reaction.ecocyc.GLYCEROL-1-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYCEROL-2-PHOSPHATASE-RXN|reaction.ecocyc.GLYCEROL-2-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14073|reaction.ecocyc.RXN-14073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17701|reaction.ecocyc.RXN-17701]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24050|reaction.ecocyc.RXN-24050]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-131|reaction.ecocyc.TRANS-RXN-131]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00847|reaction.R00847]] `KEGG` `database` - C00002 + C00116 <=> C00008 + C00093
- `is_substrate_of` --> [[reaction.ecocyc.GLYCDEH-RXN|reaction.ecocyc.GLYCDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCEROL-KIN-RXN|reaction.ecocyc.GLYCEROL-KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6467|reaction.ecocyc.RXN0-6467]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7272|reaction.ecocyc.RXN0-7272]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-131|reaction.ecocyc.TRANS-RXN-131]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-2584|reaction.ecocyc.RXN0-2584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-313|reaction.ecocyc.RXN0-313]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00116`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
