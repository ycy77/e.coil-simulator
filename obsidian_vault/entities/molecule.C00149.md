---
entity_id: "molecule.C00149"
entity_type: "small_molecule"
name: "(S)-Malate"
source_database: "KEGG"
source_id: "C00149"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-Malate"
  - "L-Malate"
  - "L-Apple acid"
  - "L-Malic acid"
  - "L-2-Hydroxybutanedioic acid"
  - "Malate"
  - "Malic acid"
---

# (S)-Malate

`molecule.C00149`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00149`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-Malate; L-Malate; L-Apple acid; L-Malic acid; L-2-Hydroxybutanedioic acid; Malate; Malic acid

## Biological Role

Consumed as substrate in 15 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: (S)-Malate; L-Malate; L-Apple acid; L-Malic acid; L-2-Hydroxybutanedioic acid; Malate; Malic acid

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (22)

- `is_product_of` --> [[reaction.ecocyc.MALSYN-RXN|reaction.ecocyc.MALSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16329|reaction.ecocyc.RXN-16329]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-106B|reaction.ecocyc.TRANS-RXN-106B]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-121A|reaction.ecocyc.TRANS-RXN-121A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00214|reaction.R00214]] `KEGG` `database` - C00149 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00216|reaction.R00216]] `KEGG` `database` - C00149 + C00006 <=> C00022 + C00011 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00342|reaction.R00342]] `KEGG` `database` - C00149 + C00003 <=> C00036 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00360|reaction.R00360]] `KEGG` `database` - C00149 + C00007 <=> C00036 + C00027
- `is_substrate_of` --> [[reaction.R00361|reaction.R00361]] `KEGG` `database` - C00149 + C15602 <=> C00036 + C15603
- `is_substrate_of` --> [[reaction.R00472|reaction.R00472]] `KEGG` `database` - C00149 + C00010 <=> C00024 + C00001 + C00048
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.39-RXN|reaction.ecocyc.1.1.1.39-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FUMHYDR-RXN|reaction.ecocyc.FUMHYDR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALATE-DEH-RXN|reaction.ecocyc.MALATE-DEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-NADP_-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16819|reaction.ecocyc.RXN-16819]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-106B|reaction.ecocyc.TRANS-RXN-106B]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-121A|reaction.ecocyc.TRANS-RXN-121A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LTARTDEHYDRA-RXN|reaction.ecocyc.LTARTDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00149`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
