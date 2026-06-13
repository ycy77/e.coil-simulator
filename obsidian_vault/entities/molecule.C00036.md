---
entity_id: "molecule.C00036"
entity_type: "small_molecule"
name: "Oxaloacetate"
source_database: "KEGG"
source_id: "C00036"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Oxaloacetate"
  - "Oxalacetic acid"
  - "Oxaloacetic acid"
  - "2-Oxobutanedioic acid"
  - "2-Oxosuccinic acid"
  - "keto-Oxaloacetate"
---

# Oxaloacetate

`molecule.C00036`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00036`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Oxaloacetate; Oxalacetic acid; Oxaloacetic acid; 2-Oxobutanedioic acid; 2-Oxosuccinic acid; keto-Oxaloacetate

## Biological Role

Consumed as substrate in 14 reaction(s). Produced in 21 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00946` Degradation of flavonoids (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Oxaloacetate; Oxalacetic acid; Oxaloacetic acid; 2-Oxobutanedioic acid; 2-Oxosuccinic acid; keto-Oxaloacetate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00946` Degradation of flavonoids (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (45)

- `activates` --> [[reaction.ecocyc.DEPHOSICITDEHASE-RXN|reaction.ecocyc.DEPHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00339|reaction.R00339]] `KEGG` `database` - C00898 <=> C00036 + C00001
- `is_product_of` --> [[reaction.R00342|reaction.R00342]] `KEGG` `database` - C00149 + C00003 <=> C00036 + C00004 + C00080
- `is_product_of` --> [[reaction.R00348|reaction.R00348]] `KEGG` `database` - C02362 + C00001 <=> C00036 + C00014
- `is_product_of` --> [[reaction.R00351|reaction.R00351]] `KEGG` `database` - C00158 + C00010 <=> C00024 + C00001 + C00036
- `is_product_of` --> [[reaction.R00354|reaction.R00354]] `KEGG` `database` - C00566 <=> C00024 + C00036
- `is_product_of` --> [[reaction.R00355|reaction.R00355]] `KEGG` `database` - C00049 + C00026 <=> C00036 + C00025
- `is_product_of` --> [[reaction.R00357|reaction.R00357]] `KEGG` `database` - C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027
- `is_product_of` --> [[reaction.R00360|reaction.R00360]] `KEGG` `database` - C00149 + C00007 <=> C00036 + C00027
- `is_product_of` --> [[reaction.R00361|reaction.R00361]] `KEGG` `database` - C00149 + C15602 <=> C00036 + C15603
- `is_product_of` --> [[reaction.ecocyc.ASPAMINOTRANS-RXN|reaction.ecocyc.ASPAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CITLY-RXN|reaction.ecocyc.CITLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CITRYLY-RXN|reaction.ecocyc.CITRYLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.D--TARTRATE-DEHYDRATASE-RXN|reaction.ecocyc.D--TARTRATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.LTARTDEHYDRA-RXN|reaction.ecocyc.LTARTDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MALATE-DEH-RXN|reaction.ecocyc.MALATE-DEH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-NADP_-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-23715|reaction.ecocyc.RXN-23715]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-9771|reaction.ecocyc.RXN-9771]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7485|reaction.ecocyc.RXN0-7485]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-226|reaction.ecocyc.TRANS-RXN-226]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00217|reaction.R00217]] `KEGG` `database` - C00036 <=> C00022 + C00011
- `is_substrate_of` --> [[reaction.R00341|reaction.R00341]] `KEGG` `database` - C00002 + C00036 <=> C00008 + C00074 + C00011
- `is_substrate_of` --> [[reaction.R00345|reaction.R00345]] `KEGG` `database` - C00009 + C00036 <=> C00001 + C00074 + C00011
- `is_substrate_of` --> [[reaction.R00363|reaction.R00363]] `KEGG` `database` - C00036 <=> C03981
- `is_substrate_of` --> [[reaction.R01731|reaction.R01731]] `KEGG` `database` - C00036 + C00826 <=> C00049 + C00254
- `is_substrate_of` --> [[reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN|reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN|reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.OXALODECARB-RXN|reaction.ecocyc.OXALODECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PEPCARBOXYKIN-RXN|reaction.ecocyc.PEPCARBOXYKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYROXALTRANSAM-RXN|reaction.ecocyc.PYROXALTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16329|reaction.ecocyc.RXN-16329]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-226|reaction.ecocyc.TRANS-RXN-226]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.1.1.39-RXN|reaction.ecocyc.1.1.1.39-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.2OXOGLUTDECARB-RXN|reaction.ecocyc.2OXOGLUTDECARB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CITLY-RXN|reaction.ecocyc.CITLY-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCITDEH-RXN|reaction.ecocyc.ISOCITDEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPSYNTH-RXN|reaction.ecocyc.PEPSYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSICITDEHASE-RXN|reaction.ecocyc.PHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.R601-RXN|reaction.ecocyc.R601-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00036`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
