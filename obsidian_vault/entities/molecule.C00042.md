---
entity_id: "molecule.C00042"
entity_type: "small_molecule"
name: "Succinate"
source_database: "KEGG"
source_id: "C00042"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Succinate"
  - "Succinic acid"
  - "Butanedionic acid"
  - "Ethylenesuccinic acid"
---

# Succinate

`molecule.C00042`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00042`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Succinate; Succinic acid; Butanedionic acid; Ethylenesuccinic acid

## Biological Role

Consumed as substrate in 13 reaction(s). Produced in 43 reaction(s).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Succinate; Succinic acid; Butanedionic acid; Ethylenesuccinic acid

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (62)

- `activates` --> [[reaction.ecocyc.DCUS-RXN|reaction.ecocyc.DCUS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` --> [[reaction.R00409|reaction.R00409]] `KEGG` `database` - C04593 <=> C00022 + C00042
- `is_product_of` --> [[reaction.R00411|reaction.R00411]] `KEGG` `database` - C05931 + C00001 <=> C00025 + C00042
- `is_product_of` --> [[reaction.R00479|reaction.R00479]] `KEGG` `database` - C00311 <=> C00042 + C00048
- `is_product_of` --> [[reaction.R00713|reaction.R00713]] `KEGG` `database` - C00232 + C00003 + C00001 <=> C00042 + C00004 + C00080
- `is_product_of` --> [[reaction.R00714|reaction.R00714]] `KEGG` `database` - C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080
- `is_product_of` --> [[reaction.R00999|reaction.R00999]] `KEGG` `database` - C01118 + C00001 <=> C00109 + C00042 + C00014
- `is_product_of` --> [[reaction.R05320|reaction.R05320]] `KEGG` `database` - C00245 + C00026 + C00007 <=> C00094 + C06735 + C00042 + C00011
- `is_product_of` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.METBALT-RXN|reaction.ecocyc.METBALT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN|reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MHPCHYDROL-RXN|reaction.ecocyc.MHPCHYDROL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN|reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.R601-RXN|reaction.ecocyc.R601-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12353|reaction.ecocyc.RXN-12353]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15147|reaction.ecocyc.RXN-15147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18737|reaction.ecocyc.RXN-18737]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18738|reaction.ecocyc.RXN-18738]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18739|reaction.ecocyc.RXN-18739]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21233|reaction.ecocyc.RXN-21233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21235|reaction.ecocyc.RXN-21235]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21236|reaction.ecocyc.RXN-21236]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-9772|reaction.ecocyc.RXN-9772]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-299|reaction.ecocyc.RXN0-299]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5245|reaction.ecocyc.RXN0-5245]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7090|reaction.ecocyc.RXN0-7090]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7275|reaction.ecocyc.RXN0-7275]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7280|reaction.ecocyc.RXN0-7280]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7316|reaction.ecocyc.RXN0-7316]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7484|reaction.ecocyc.RXN0-7484]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-984|reaction.ecocyc.RXN0-984]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-986|reaction.ecocyc.RXN0-986]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCDIAMINOPIMDESUCC-RXN|reaction.ecocyc.SUCCDIAMINOPIMDESUCC-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCGLUDESUCC-RXN|reaction.ecocyc.SUCCGLUDESUCC-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN|reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-106|reaction.ecocyc.TRANS-RXN-106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-106A|reaction.ecocyc.TRANS-RXN-106A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-106B|reaction.ecocyc.TRANS-RXN-106B]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-121|reaction.ecocyc.TRANS-RXN-121]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-127|reaction.ecocyc.TRANS-RXN-127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-300|reaction.ecocyc.TRANS-RXN-300]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-201|reaction.ecocyc.TRANS-RXN0-201]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-499|reaction.ecocyc.TRANS-RXN0-499]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00405|reaction.R00405]] `KEGG` `database` - C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091
- `is_substrate_of` --> [[reaction.R02603|reaction.R02603]] `KEGG` `database` - C00596 + C00042 <=> C04479 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-268|reaction.ecocyc.RXN0-268]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCCOASYN-RXN|reaction.ecocyc.SUCCCOASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN|reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-106|reaction.ecocyc.TRANS-RXN-106]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-106A|reaction.ecocyc.TRANS-RXN-106A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-106B|reaction.ecocyc.TRANS-RXN-106B]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-121|reaction.ecocyc.TRANS-RXN-121]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-127|reaction.ecocyc.TRANS-RXN-127]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-300|reaction.ecocyc.TRANS-RXN-300]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-201|reaction.ecocyc.TRANS-RXN0-201]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-499|reaction.ecocyc.TRANS-RXN0-499]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ASPCARBTRANS-RXN|reaction.ecocyc.ASPCARBTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-18737|reaction.ecocyc.RXN-18737]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (5)

- `transports` <-- [[protein.P0ABN9|protein.P0ABN9]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0ABP3|protein.P0ABP3]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AE74|protein.P0AE74]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AFR2|protein.P0AFR2]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P39414|protein.P39414]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00042`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
