---
entity_id: "molecule.C00092"
entity_type: "small_molecule"
name: "D-Glucose 6-phosphate"
source_database: "KEGG"
source_id: "C00092"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glucose 6-phosphate"
  - "Glucose 6-phosphate"
  - "Robison ester"
  - "D-glucose-6-P"
---

# D-Glucose 6-phosphate

`molecule.C00092`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00092`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glucose 6-phosphate; Glucose 6-phosphate; Robison ester EcoCyc common name: D-glucopyranose 6-phosphate.

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 10 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Glucose 6-phosphate; Glucose 6-phosphate; Robison ester

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (19)

- `activates` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00299|reaction.R00299]] `KEGG` `database` - C00002 + C00031 <=> C00008 + C00092
- `is_product_of` --> [[reaction.R00837|reaction.R00837]] `KEGG` `database` - C00001 + C00689 <=> C00031 + C00092
- `is_product_of` --> [[reaction.R00839|reaction.R00839]] `KEGG` `database` - C04534 + C00001 <=> C00031 + C00092
- `is_product_of` --> [[reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN|reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUCOKIN-RXN|reaction.ecocyc.GLUCOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSPHOGLUCMUT-RXN|reaction.ecocyc.PHOSPHOGLUCMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16998|reaction.ecocyc.RXN-16998]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-157|reaction.ecocyc.TRANS-RXN-157]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-33|reaction.ecocyc.TRANS-RXN-33]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRE6PHYDRO-RXN|reaction.ecocyc.TRE6PHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00771|reaction.R00771]] `KEGG` `database` - C00092 <=> C00085
- `is_substrate_of` --> [[reaction.R00835|reaction.R00835]] `KEGG` `database` - C00092 + C00006 <=> C01236 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00836|reaction.R00836]] `KEGG` `database` - C00029 + C00092 <=> C00015 + C00689
- `is_substrate_of` --> [[reaction.ecocyc.GLU6PDEHYDROG-RXN|reaction.ecocyc.GLU6PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7362|reaction.ecocyc.RXN0-7362]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN66-526|reaction.ecocyc.RXN66-526]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-33|reaction.ecocyc.TRANS-RXN-33]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TREHALOSE6PSYN-RXN|reaction.ecocyc.TREHALOSE6PSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AGC0|protein.P0AGC0]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00092`
- `EcoCyc:Glucose-6-phosphate`
- `METANETX:MNXM149016`
- `canonicalized_from:molecule.ecocyc.Glucose-6-phosphate`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.Glucose-6-phosphate: EcoCyc:Glucose-6-phosphate
