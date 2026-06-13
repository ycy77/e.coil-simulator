---
entity_id: "molecule.C01172"
entity_type: "small_molecule"
name: "beta-D-Glucose 6-phosphate"
source_database: "KEGG"
source_id: "C01172"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "beta-D-Glucose 6-phosphate"
---

# beta-D-Glucose 6-phosphate

`molecule.C01172`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01172`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: beta-D-Glucose 6-phosphate EcoCyc common name: β-D-glucose 6-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)

## Annotation

KEGG compound: beta-D-Glucose 6-phosphate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)

## Outgoing Edges (12)

- `activates` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.BETA-PHOSPHOGLUCOMUTASE-RXN|reaction.ecocyc.BETA-PHOSPHOGLUCOMUTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUCOSE-6-PHOSPHATE-1-EPIMERASE-RXN|reaction.ecocyc.GLUCOSE-6-PHOSPHATE-1-EPIMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16996|reaction.ecocyc.RXN-16996]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5295|reaction.ecocyc.RXN0-5295]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5297|reaction.ecocyc.RXN0-5297]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6994|reaction.ecocyc.RXN0-6994]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-963|reaction.ecocyc.RXN0-963]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R10907|reaction.R10907]] `KEGG` `database` - C01172 + C00003 <=> C01236 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.GLUCOSE-6-PHOSPHATASE-RXN|reaction.ecocyc.GLUCOSE-6-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UHPC-RXN|reaction.ecocyc.UHPC-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01172`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
