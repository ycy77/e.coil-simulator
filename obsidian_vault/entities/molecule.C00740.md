---
entity_id: "molecule.C00740"
entity_type: "small_molecule"
name: "D-Serine"
source_database: "KEGG"
source_id: "C00740"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Serine"
---

# D-Serine

`molecule.C00740`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00740`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Serine

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: D-Serine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (15)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7714|complex.ecocyc.CPLX0-7714]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00589|reaction.R00589]] `KEGG` `database` - C00065 <=> C00740
- `is_product_of` --> [[reaction.R02853|reaction.R02853]] `KEGG` `database` - C02532 + C00001 <=> C00740 + C00009
- `is_product_of` --> [[reaction.ecocyc.RXN0-5130|reaction.ecocyc.RXN0-5130]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-495|reaction.ecocyc.TRANS-RXN0-495]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00221|reaction.R00221]] `KEGG` `database` - C00740 <=> C00022 + C00014
- `is_substrate_of` --> [[reaction.ecocyc.DSERDEAM-RXN|reaction.ecocyc.DSERDEAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15581|reaction.ecocyc.RXN-15581]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5130|reaction.ecocyc.RXN0-5130]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5389|reaction.ecocyc.RXN0-5389]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-495|reaction.ecocyc.TRANS-RXN0-495]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.4.3.1.17-RXN|reaction.ecocyc.4.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ASPDECARBOX-RXN|reaction.ecocyc.ASPDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-469|reaction.ecocyc.TRANS-RXN0-469]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AAE0|protein.P0AAE0]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00740`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
