---
entity_id: "molecule.C00231"
entity_type: "small_molecule"
name: "D-Xylulose 5-phosphate"
source_database: "KEGG"
source_id: "C00231"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Xylulose 5-phosphate"
---

# D-Xylulose 5-phosphate

`molecule.C00231`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00231`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Xylulose 5-phosphate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Annotation

KEGG compound: D-Xylulose 5-phosphate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R01529|reaction.R01529]] `KEGG` `database` - C00199 <=> C00231
- `is_product_of` --> [[reaction.R05850|reaction.R05850]] `KEGG` `database` - C01101 <=> C00231
- `is_product_of` --> [[reaction.ecocyc.1TRANSKETO-RXN|reaction.ecocyc.1TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBULP3EPIM-RXN|reaction.ecocyc.RIBULP3EPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBULPEPIM-RXN|reaction.ecocyc.RIBULPEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.XYLULOKIN-RXN|reaction.ecocyc.XYLULOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.2TRANSKETO-RXN|reaction.ecocyc.2TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00231`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
