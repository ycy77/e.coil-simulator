---
entity_id: "molecule.C00118"
entity_type: "small_molecule"
name: "D-Glyceraldehyde 3-phosphate"
source_database: "KEGG"
source_id: "C00118"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glyceraldehyde 3-phosphate"
  - "(2R)-2-Hydroxy-3-(phosphonooxy)-propanal"
  - "Glyceraldehyde 3-phosphate"
---

# D-Glyceraldehyde 3-phosphate

`molecule.C00118`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00118`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glyceraldehyde 3-phosphate; (2R)-2-Hydroxy-3-(phosphonooxy)-propanal; Glyceraldehyde 3-phosphate

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 10 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Annotation

KEGG compound: D-Glyceraldehyde 3-phosphate; (2R)-2-Hydroxy-3-(phosphonooxy)-propanal; Glyceraldehyde 3-phosphate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Outgoing Edges (19)

- `is_product_of` --> [[reaction.R02340|reaction.R02340]] `KEGG` `database` - C03506 <=> C00463 + C00118
- `is_product_of` --> [[reaction.ecocyc.2TRANSKETO-RXN|reaction.ecocyc.2TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DEHYDDEOXPHOSGALACT-ALDOL-RXN|reaction.ecocyc.DEHYDDEOXPHOSGALACT-ALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DEOXYRIBOSE-P-ALD-RXN|reaction.ecocyc.DEOXYRIBOSE-P-ALD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.F16ALDOLASE-RXN|reaction.ecocyc.F16ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.KDPGALDOL-RXN|reaction.ecocyc.KDPGALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2381|reaction.ecocyc.RXN0-2381]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-313|reaction.ecocyc.RXN0-313]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TAGAALDOL-RXN|reaction.ecocyc.TAGAALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRYPSYN-RXN|reaction.ecocyc.TRYPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01015|reaction.R01015]] `KEGG` `database` - C00118 <=> C00111
- `is_substrate_of` --> [[reaction.ecocyc.1TRANSKETO-RXN|reaction.ecocyc.1TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DXS-RXN|reaction.ecocyc.DXS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GAPOXNPHOSPHN-RXN|reaction.ecocyc.GAPOXNPHOSPHN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7250|reaction.ecocyc.RXN0-7250]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANSALDOL-RXN|reaction.ecocyc.TRANSALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRIOSEPISOMERIZATION-RXN|reaction.ecocyc.TRIOSEPISOMERIZATION-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDPGALDOL-RXN|reaction.ecocyc.KDPGALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00118`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
