---
entity_id: "molecule.C00091"
entity_type: "small_molecule"
name: "Succinyl-CoA"
source_database: "KEGG"
source_id: "C00091"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Succinyl-CoA"
  - "Succinyl coenzyme A"
---

# Succinyl-CoA

`molecule.C00091`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00091`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Succinyl-CoA; Succinyl coenzyme A

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco00984` Steroid degradation (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

KEGG compound: Succinyl-CoA; Succinyl coenzyme A

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco00984` Steroid degradation (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Outgoing Edges (14)

- `is_product_of` --> [[reaction.R00405|reaction.R00405]] `KEGG` `database` - C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091
- `is_product_of` --> [[reaction.R00833|reaction.R00833]] `KEGG` `database` - C01213 <=> C00091
- `is_product_of` --> [[reaction.ecocyc.2OXOGLUTARATEDEH-RXN|reaction.ecocyc.2OXOGLUTARATEDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.METHYLMALONYL-COA-MUT-RXN|reaction.ecocyc.METHYLMALONYL-COA-MUT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-268|reaction.ecocyc.RXN0-268]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCCOASYN-RXN|reaction.ecocyc.SUCCCOASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00829|reaction.R00829]] `KEGG` `database` - C00091 + C00024 <=> C00010 + C02232
- `is_substrate_of` --> [[reaction.R00832|reaction.R00832]] `KEGG` `database` - C00091 + C00062 <=> C00010 + C03296
- `is_substrate_of` --> [[reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN|reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HOMSUCTRAN-RXN|reaction.ecocyc.HOMSUCTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-3641|reaction.ecocyc.RXN-3641]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1147|reaction.ecocyc.RXN0-1147]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TETHYDPICSUCC-RXN|reaction.ecocyc.TETHYDPICSUCC-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00091`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
