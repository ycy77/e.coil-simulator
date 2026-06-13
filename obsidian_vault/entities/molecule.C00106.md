---
entity_id: "molecule.C00106"
entity_type: "small_molecule"
name: "Uracil"
source_database: "KEGG"
source_id: "C00106"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Uracil"
---

# Uracil

`molecule.C00106`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00106`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Uracil

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 11 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: Uracil

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (20)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7651|complex.ecocyc.CPLX0-7651]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00977|reaction.R00977]] `KEGG` `database` - C00429 + C00003 <=> C00106 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.CYTDEAM-RXN|reaction.ecocyc.CYTDEAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN|reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21261|reaction.ecocyc.RXN-21261]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2584|reaction.ecocyc.RXN0-2584]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-132|reaction.ecocyc.TRANS-RXN-132]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-560|reaction.ecocyc.TRANS-RXN0-560]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URA-PHOSPH-RXN|reaction.ecocyc.URA-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN|reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN|reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URPHOS-RXN|reaction.ecocyc.URPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20707|reaction.ecocyc.RXN-20707]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5332|reaction.ecocyc.RXN0-5332]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5398|reaction.ecocyc.RXN0-5398]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6444|reaction.ecocyc.RXN0-6444]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-132|reaction.ecocyc.TRANS-RXN-132]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-560|reaction.ecocyc.TRANS-RXN0-560]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-2584|reaction.ecocyc.RXN0-2584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.URPHOS-RXN|reaction.ecocyc.URPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P75892|protein.P75892]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00106`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
