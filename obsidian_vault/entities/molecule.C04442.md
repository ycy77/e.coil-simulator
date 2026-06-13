---
entity_id: "molecule.C04442"
entity_type: "small_molecule"
name: "2-Dehydro-3-deoxy-6-phospho-D-gluconate"
source_database: "KEGG"
source_id: "C04442"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Dehydro-3-deoxy-6-phospho-D-gluconate"
  - "6-Phospho-2-dehydro-3-deoxy-D-gluconate"
  - "2-Keto-3-deoxy-6-phosphogluconate"
  - "2-Dehydro-3-deoxy-D-gluconate 6-phosphate"
---

# 2-Dehydro-3-deoxy-6-phospho-D-gluconate

`molecule.C04442`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04442`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Dehydro-3-deoxy-6-phospho-D-gluconate; 6-Phospho-2-dehydro-3-deoxy-D-gluconate; 2-Keto-3-deoxy-6-phosphogluconate; 2-Dehydro-3-deoxy-D-gluconate 6-phosphate EcoCyc common name: 2-dehydro-3-deoxy-D-gluconate 6-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Annotation

KEGG compound: 2-Dehydro-3-deoxy-6-phospho-D-gluconate; 6-Phospho-2-dehydro-3-deoxy-D-gluconate; 2-Keto-3-deoxy-6-phosphogluconate; 2-Dehydro-3-deoxy-D-gluconate 6-phosphate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Outgoing Edges (7)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8162|complex.ecocyc.CPLX0-8162]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R01541|reaction.R01541]] `KEGG` `database` - C00002 + C00204 <=> C00008 + C04442
- `is_product_of` --> [[reaction.ecocyc.DEOXYGLUCONOKIN-RXN|reaction.ecocyc.DEOXYGLUCONOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PGLUCONDEHYDRAT-RXN|reaction.ecocyc.PGLUCONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.KDPGALDOL-RXN|reaction.ecocyc.KDPGALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7159|reaction.ecocyc.RXN0-7159]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDGALDOL-RXN|reaction.ecocyc.KDGALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04442`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
