---
entity_id: "molecule.C00158"
entity_type: "small_molecule"
name: "Citrate"
source_database: "KEGG"
source_id: "C00158"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Citrate"
  - "Citric acid"
  - "2-Hydroxy-1,2,3-propanetricarboxylic acid"
  - "2-Hydroxytricarballylic acid"
---

# Citrate

`molecule.C00158`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00158`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Citrate; Citric acid; 2-Hydroxy-1,2,3-propanetricarboxylic acid; 2-Hydroxytricarballylic acid

## Biological Role

Consumed as substrate in 9 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Citrate; Citric acid; 2-Hydroxy-1,2,3-propanetricarboxylic acid; 2-Hydroxytricarballylic acid

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (21)

- `activates` --> [[reaction.ecocyc.F16ALDOLASE-RXN|reaction.ecocyc.F16ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-6271|reaction.ecocyc.RXN0-6271]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-201|reaction.ecocyc.TRANS-RXN0-201]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00351|reaction.R00351]] `KEGG` `database` - C00158 + C00010 <=> C00024 + C00001 + C00036
- `is_substrate_of` --> [[reaction.R01323|reaction.R01323]] `KEGG` `database` - C00024 + C00158 <=> C00033 + C00566
- `is_substrate_of` --> [[reaction.R01324|reaction.R01324]] `KEGG` `database` - C00158 <=> C00311
- `is_substrate_of` --> [[reaction.R01325|reaction.R01325]] `KEGG` `database` - C00158 <=> C00417 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.ACONITATEDEHYDR-RXN|reaction.ecocyc.ACONITATEDEHYDR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CITLY-RXN|reaction.ecocyc.CITLY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CITTRANS-RXN|reaction.ecocyc.CITTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14047|reaction.ecocyc.RXN-14047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-201|reaction.ecocyc.TRANS-RXN0-201]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.6PFRUCTPHOS-RXN|reaction.ecocyc.6PFRUCTPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CHORISMATEMUT-RXN|reaction.ecocyc.CHORISMATEMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.FUMHYDR-RXN|reaction.ecocyc.FUMHYDR-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSICITDEHASE-RXN|reaction.ecocyc.PHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-13990|reaction.ecocyc.RXN-13990]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00158`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
