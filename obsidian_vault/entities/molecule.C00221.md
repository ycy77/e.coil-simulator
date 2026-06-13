---
entity_id: "molecule.C00221"
entity_type: "small_molecule"
name: "beta-D-Glucose"
source_database: "KEGG"
source_id: "C00221"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "beta-D-Glucose"
  - "beta-D-Glucopyranose"
---

# beta-D-Glucose

`molecule.C00221`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00221`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: beta-D-Glucose; beta-D-Glucopyranose EcoCyc common name: β-D-glucopyranose.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)

## Annotation

KEGG compound: beta-D-Glucose; beta-D-Glucopyranose

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.R00026|reaction.R00026]] `KEGG` `database` - C00185 + C00001 <=> 2 C00221
- `is_product_of` --> [[reaction.R13051|reaction.R13051]] `KEGG` `database` - C10216 + C00001 <=> C10208 + C00221
- `is_product_of` --> [[reaction.R13052|reaction.R13052]] `KEGG` `database` - C09126 + C00001 <=> C06563 + C00221
- `is_product_of` --> [[reaction.R13065|reaction.R13065]] `KEGG` `database` - C05623 + C00001 <=> C00389 + C00221
- `is_product_of` --> [[reaction.R13081|reaction.R13081]] `KEGG` `database` - C09099 + C00001 <=> C00509 + C00221
- `is_product_of` --> [[reaction.ecocyc.ALDOSE-1-EPIMERASE-RXN|reaction.ecocyc.ALDOSE-1-EPIMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUCOSE-6-PHOSPHATASE-RXN|reaction.ecocyc.GLUCOSE-6-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TREHALA-RXN|reaction.ecocyc.TREHALA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6418|reaction.ecocyc.RXN0-6418]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLYCOPHOSPHORYL-RXN|reaction.ecocyc.GLYCOPHOSPHORYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00221`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
