---
entity_id: "molecule.C00049"
entity_type: "small_molecule"
name: "L-Aspartate"
source_database: "KEGG"
source_id: "C00049"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Aspartate"
  - "L-Aspartic acid"
  - "2-Aminosuccinic acid"
  - "L-Asp"
---

# L-Aspartate

`molecule.C00049`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00049`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Aspartate; L-Aspartic acid; 2-Aminosuccinic acid; L-Asp

## Biological Role

Consumed as substrate in 28 reaction(s). Produced in 12 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

KEGG compound: L-Aspartate; L-Aspartic acid; 2-Aminosuccinic acid; L-Asp

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (48)

- `activates` --> [[reaction.ecocyc.1.1.1.39-RXN|reaction.ecocyc.1.1.1.39-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.ASPARTASE-RXN|reaction.ecocyc.ASPARTASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00485|reaction.R00485]] `KEGG` `database` - C00152 + C00001 <=> C00049 + C00014
- `is_product_of` --> [[reaction.R01731|reaction.R01731]] `KEGG` `database` - C00036 + C00826 <=> C00049 + C00254
- `is_product_of` --> [[reaction.ecocyc.3.4.13.21-RXN|reaction.ecocyc.3.4.13.21-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ASPARAGHYD-RXN|reaction.ecocyc.ASPARAGHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYROXALTRANSAM-RXN|reaction.ecocyc.PYROXALTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3241|reaction.ecocyc.RXN0-3241]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6975|reaction.ecocyc.RXN0-6975]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6987|reaction.ecocyc.RXN0-6987]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-106A|reaction.ecocyc.TRANS-RXN-106A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-122A|reaction.ecocyc.TRANS-RXN-122A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-379|reaction.ecocyc.TRANS-RXN-379]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-222|reaction.ecocyc.TRANS-RXN0-222]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00355|reaction.R00355]] `KEGG` `database` - C00049 + C00026 <=> C00036 + C00025
- `is_substrate_of` --> [[reaction.R00357|reaction.R00357]] `KEGG` `database` - C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027
- `is_substrate_of` --> [[reaction.R00480|reaction.R00480]] `KEGG` `database` - C00002 + C00049 <=> C00008 + C03082
- `is_substrate_of` --> [[reaction.R00481|reaction.R00481]] `KEGG` `database` - C00049 + C00007 <=> C05840 + C00027
- `is_substrate_of` --> [[reaction.R00483|reaction.R00483]] `KEGG` `database` - C00002 + C00049 + C00014 <=> C00020 + C00013 + C00152
- `is_substrate_of` --> [[reaction.R00489|reaction.R00489]] `KEGG` `database` - C00049 <=> C00099 + C00011
- `is_substrate_of` --> [[reaction.R00490|reaction.R00490]] `KEGG` `database` - C00049 <=> C00122 + C00014
- `is_substrate_of` --> [[reaction.R00578|reaction.R00578]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_substrate_of` --> [[reaction.R01135|reaction.R01135]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_substrate_of` --> [[reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN|reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ARGSUCCINSYN-RXN|reaction.ecocyc.ARGSUCCINSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASNSYNA-RXN|reaction.ecocyc.ASNSYNA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASNSYNB-RXN|reaction.ecocyc.ASNSYNB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASPAMINOTRANS-RXN|reaction.ecocyc.ASPAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASPARTASE-RXN|reaction.ecocyc.ASPARTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASPARTATE--TRNA-LIGASE-RXN|reaction.ecocyc.ASPARTATE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASPARTATEKIN-RXN|reaction.ecocyc.ASPARTATEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASPCARBTRANS-RXN|reaction.ecocyc.ASPCARBTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASPDECARBOX-RXN|reaction.ecocyc.ASPDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.L-ASPARTATE-OXID-RXN|reaction.ecocyc.L-ASPARTATE-OXID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14814|reaction.ecocyc.RXN-14814]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22734|reaction.ecocyc.RXN-22734]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9772|reaction.ecocyc.RXN-9772]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SAICARSYN-RXN|reaction.ecocyc.SAICARSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-106A|reaction.ecocyc.TRANS-RXN-106A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-122A|reaction.ecocyc.TRANS-RXN-122A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-379|reaction.ecocyc.TRANS-RXN-379]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-222|reaction.ecocyc.TRANS-RXN0-222]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ASPARAGHYD-RXN|reaction.ecocyc.ASPARAGHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTAMATESYN-RXN|reaction.ecocyc.GLUTAMATESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYROXALTRANSAM-RXN|reaction.ecocyc.PYROXALTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN-57|reaction.ecocyc.TRANS-RXN-57]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (3)

- `transports` <-- [[complex.ecocyc.ABC-13-CPLX|complex.ecocyc.ABC-13-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0ABN5|protein.P0ABN5]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AFR2|protein.P0AFR2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00049`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
