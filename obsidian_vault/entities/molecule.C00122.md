---
entity_id: "molecule.C00122"
entity_type: "small_molecule"
name: "Fumarate"
source_database: "KEGG"
source_id: "C00122"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Fumarate"
  - "Fumaric acid"
  - "trans-Butenedioic acid"
---

# Fumarate

`molecule.C00122`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00122`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Fumarate; Fumaric acid; trans-Butenedioic acid

## Biological Role

Consumed as substrate in 9 reaction(s). Produced in 12 reaction(s).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Fumarate; Fumaric acid; trans-Butenedioic acid

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (25)

- `activates` --> [[reaction.ecocyc.DCUS-RXN|reaction.ecocyc.DCUS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` --> [[reaction.R00490|reaction.R00490]] `KEGG` `database` - C00049 <=> C00122 + C00014
- `is_product_of` --> [[reaction.ecocyc.AICARSYN-RXN|reaction.ecocyc.AICARSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.AMPSYN-RXN|reaction.ecocyc.AMPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ARGSUCCINLYA-RXN|reaction.ecocyc.ARGSUCCINLYA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ASPARTASE-RXN|reaction.ecocyc.ASPARTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.FUMHYDR-RXN|reaction.ecocyc.FUMHYDR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12070|reaction.ecocyc.RXN-12070]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN|reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-106|reaction.ecocyc.TRANS-RXN-106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-299|reaction.ecocyc.TRANS-RXN-299]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-379|reaction.ecocyc.TRANS-RXN-379]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-553|reaction.ecocyc.TRANS-RXN0-553]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.R601-RXN|reaction.ecocyc.R601-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22606|reaction.ecocyc.RXN-22606]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22643|reaction.ecocyc.RXN-22643]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9772|reaction.ecocyc.RXN-9772]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5245|reaction.ecocyc.RXN0-5245]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-106|reaction.ecocyc.TRANS-RXN-106]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-299|reaction.ecocyc.TRANS-RXN-299]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-379|reaction.ecocyc.TRANS-RXN-379]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-553|reaction.ecocyc.TRANS-RXN0-553]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-18737|reaction.ecocyc.RXN-18737]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0ABN5|protein.P0ABN5]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00122`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
