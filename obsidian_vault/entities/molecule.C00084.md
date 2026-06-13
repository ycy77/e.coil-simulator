---
entity_id: "molecule.C00084"
entity_type: "small_molecule"
name: "Acetaldehyde"
source_database: "KEGG"
source_id: "C00084"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acetaldehyde"
  - "Ethanal"
---

# Acetaldehyde

`molecule.C00084`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00084`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acetaldehyde; Ethanal

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 15 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: Acetaldehyde; Ethanal

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (25)

- `is_product_of` --> [[reaction.R00746|reaction.R00746]] `KEGG` `database` - C00469 + C00006 <=> C00084 + C00005 + C00080
- `is_product_of` --> [[reaction.R00749|reaction.R00749]] `KEGG` `database` - C00189 <=> C00084 + C00014
- `is_product_of` --> [[reaction.R00751|reaction.R00751]] `KEGG` `database` - C00188 <=> C00037 + C00084
- `is_product_of` --> [[reaction.R00754|reaction.R00754]] `KEGG` `database` - C00469 + C00003 <=> C00084 + C00004 + C00080
- `is_product_of` --> [[reaction.R06171|reaction.R06171]] `KEGG` `database` - C05519 <=> C00037 + C00084
- `is_product_of` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DEOXYRIBOSE-P-ALD-RXN|reaction.ecocyc.DEOXYRIBOSE-P-ALD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ETHAMLY-RXN|reaction.ecocyc.ETHAMLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.LTAA-RXN|reaction.ecocyc.LTAA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MHPELY-RXN|reaction.ecocyc.MHPELY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-6161|reaction.ecocyc.RXN-6161]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5234|reaction.ecocyc.RXN0-5234]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5507|reaction.ecocyc.RXN0-5507]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-986|reaction.ecocyc.RXN0-986]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THREONINE-ALDOLASE-RXN|reaction.ecocyc.THREONINE-ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00228|reaction.R00228]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00750|reaction.R00750]] `KEGG` `database` - C00084 + C00022 <=> C03589
- `is_substrate_of` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9560|reaction.ecocyc.RXN-9560]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2022|reaction.ecocyc.RXN0-2022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3962|reaction.ecocyc.RXN0-3962]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN3O-470|reaction.ecocyc.RXN3O-470]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.BADH-RXN|reaction.ecocyc.BADH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-13990|reaction.ecocyc.RXN-13990]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00084`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
