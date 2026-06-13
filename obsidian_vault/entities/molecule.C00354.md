---
entity_id: "molecule.C00354"
entity_type: "small_molecule"
name: "D-Fructose 1,6-bisphosphate"
source_database: "KEGG"
source_id: "C00354"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Fructose 1,6-bisphosphate"
---

# D-Fructose 1,6-bisphosphate

`molecule.C00354`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00354`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Fructose 1,6-bisphosphate EcoCyc common name: β-D-fructofuranose 1,6-bisphosphate. The β-D-form of fructose 1,6-bisphosphate is a very common metabolite.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Fructose 1,6-bisphosphate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (18)

- `activates` --> [[reaction.ecocyc.GLUC1PADENYLTRANS-RXN|reaction.ecocyc.GLUC1PADENYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00756|reaction.R00756]] `KEGG` `database` - C00002 + C00085 <=> C00008 + C00354
- `is_product_of` --> [[reaction.R00767|reaction.R00767]] `KEGG` `database` - C00063 + C00085 <=> C00112 + C00354
- `is_product_of` --> [[reaction.R00769|reaction.R00769]] `KEGG` `database` - C00075 + C00085 <=> C00015 + C00354
- `is_product_of` --> [[reaction.R00770|reaction.R00770]] `KEGG` `database` - C00081 + C00085 <=> C00104 + C00354
- `is_product_of` --> [[reaction.ecocyc.1PFRUCTPHOSN-RXN|reaction.ecocyc.1PFRUCTPHOSN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.6PFRUCTPHOS-RXN|reaction.ecocyc.6PFRUCTPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00762|reaction.R00762]] `KEGG` `database` - C00354 + C00001 <=> C00085 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.F16ALDOLASE-RXN|reaction.ecocyc.F16ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1PFRUCTPHOSN-RXN|reaction.ecocyc.1PFRUCTPHOSN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.6PFRUCTPHOS-RXN|reaction.ecocyc.6PFRUCTPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYCEROL-KIN-RXN|reaction.ecocyc.GLYCEROL-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.QUINOPRIBOTRANS-RXN|reaction.ecocyc.QUINOPRIBOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-9952|reaction.ecocyc.RXN-9952]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00354`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
