---
entity_id: "molecule.C00148"
entity_type: "small_molecule"
name: "L-Proline"
source_database: "KEGG"
source_id: "C00148"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Proline"
  - "2-Pyrrolidinecarboxylic acid"
---

# L-Proline

`molecule.C00148`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00148`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Proline; 2-Pyrrolidinecarboxylic acid

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Proline; 2-Pyrrolidinecarboxylic acid

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (16)

- `is_product_of` --> [[reaction.ecocyc.3.4.13.9-RXN|reaction.ecocyc.3.4.13.9-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ABC-26-RXN|reaction.ecocyc.ABC-26-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6988|reaction.ecocyc.RXN0-6988]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7005|reaction.ecocyc.RXN0-7005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-118|reaction.ecocyc.TRANS-RXN-118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-29|reaction.ecocyc.TRANS-RXN-29]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03661|reaction.R03661]] `KEGG` `database` - C00002 + C00148 + C01649 <=> C00020 + C00013 + C02702
- `is_substrate_of` --> [[reaction.ecocyc.ABC-26-RXN|reaction.ecocyc.ABC-26-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PROLINE--TRNA-LIGASE-RXN|reaction.ecocyc.PROLINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRROLINECARBREDUCT-RXN|reaction.ecocyc.PYRROLINECARBREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19079|reaction.ecocyc.RXN-19079]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7008|reaction.ecocyc.RXN0-7008]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-118|reaction.ecocyc.TRANS-RXN-118]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-29|reaction.ecocyc.TRANS-RXN-29]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTKIN-RXN|reaction.ecocyc.GLUTKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYRROLINECARBREDUCT-RXN|reaction.ecocyc.PYRROLINECARBREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (3)

- `transports` <-- [[complex.ecocyc.ABC-26-CPLX|complex.ecocyc.ABC-26-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-7642|complex.ecocyc.CPLX0-7642]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P07117|protein.P07117]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00148`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
