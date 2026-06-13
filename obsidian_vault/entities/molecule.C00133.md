---
entity_id: "molecule.C00133"
entity_type: "small_molecule"
name: "D-Alanine"
source_database: "KEGG"
source_id: "C00133"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Alanine"
  - "D-2-Aminopropionic acid"
  - "D-Ala"
---

# D-Alanine

`molecule.C00133`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00133`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Alanine; D-2-Aminopropionic acid; D-Ala

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 18 reaction(s).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Annotation

KEGG compound: D-Alanine; D-2-Aminopropionic acid; D-Ala

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Outgoing Edges (26)

- `is_product_of` --> [[reaction.R00401|reaction.R00401]] `KEGG` `database` - C00041 <=> C00133
- `is_product_of` --> [[reaction.ecocyc.3.4.13.22-RXN|reaction.ecocyc.3.4.13.22-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.3.4.17.8-RXN|reaction.ecocyc.3.4.17.8-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ALARACECAT-RXN|reaction.ecocyc.ALARACECAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16649|reaction.ecocyc.RXN-16649]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16659|reaction.ecocyc.RXN-16659]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16664|reaction.ecocyc.RXN-16664]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16665|reaction.ecocyc.RXN-16665]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19249|reaction.ecocyc.RXN-19249]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19253|reaction.ecocyc.RXN-19253]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19256|reaction.ecocyc.RXN-19256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2061|reaction.ecocyc.RXN0-2061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5227|reaction.ecocyc.RXN0-5227]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5401|reaction.ecocyc.RXN0-5401]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6684|reaction.ecocyc.RXN0-6684]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7489|reaction.ecocyc.RXN0-7489]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-313|reaction.ecocyc.TRANS-RXN-313]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-62A|reaction.ecocyc.TRANS-RXN-62A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01150|reaction.R01150]] `KEGG` `database` - C00002 + 2 C00133 <=> C00008 + C00009 + C00993
- `is_substrate_of` --> [[reaction.ecocyc.DALADALALIG-RXN|reaction.ecocyc.DALADALALIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DALADEHYDROG-RXN|reaction.ecocyc.DALADEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5240|reaction.ecocyc.RXN0-5240]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-313|reaction.ecocyc.TRANS-RXN-313]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-62A|reaction.ecocyc.TRANS-RXN-62A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLYOHMETRANS-RXN|reaction.ecocyc.GLYOHMETRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-469|reaction.ecocyc.TRANS-RXN0-469]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AAE0|protein.P0AAE0]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00133`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
