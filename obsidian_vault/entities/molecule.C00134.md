---
entity_id: "molecule.C00134"
entity_type: "small_molecule"
name: "Putrescine"
source_database: "KEGG"
source_id: "C00134"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Putrescine"
  - "1,4-Butanediamine"
  - "1,4-Diaminobutane"
  - "Tetramethylenediamine"
  - "Butane-1,4-diamine"
---

# Putrescine

`molecule.C00134`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00134`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Putrescine; 1,4-Butanediamine; 1,4-Diaminobutane; Tetramethylenediamine; Butane-1,4-diamine

## Biological Role

Consumed as substrate in 10 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Putrescine; 1,4-Butanediamine; 1,4-Diaminobutane; Tetramethylenediamine; Butane-1,4-diamine

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (27)

- `activates` --> [[gene.b2684|gene.b2684]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Translation
- `is_component_of` --> [[complex.ecocyc.CPLX0-8085|complex.ecocyc.CPLX0-8085]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-9742|complex.ecocyc.CPLX0-9742]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00670|reaction.R00670]] `KEGG` `database` - C00077 <=> C00134 + C00011
- `is_product_of` --> [[reaction.R01157|reaction.R01157]] `KEGG` `database` - C00179 + C00001 <=> C00134 + C00086
- `is_product_of` --> [[reaction.ecocyc.ABC-25-RXN|reaction.ecocyc.ABC-25-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.AGMATIN-RXN|reaction.ecocyc.AGMATIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-328|reaction.ecocyc.TRANS-RXN-328]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-69|reaction.ecocyc.TRANS-RXN-69]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-211|reaction.ecocyc.TRANS-RXN0-211]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01154|reaction.R01154]] `KEGG` `database` - C00024 + C00134 <=> C00010 + C02714
- `is_substrate_of` --> [[reaction.R01155|reaction.R01155]] `KEGG` `database` - C00134 + C00026 <=> C00555 + C00025
- `is_substrate_of` --> [[reaction.ecocyc.2.6.1.82-RXN|reaction.ecocyc.2.6.1.82-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-25-RXN|reaction.ecocyc.ABC-25-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PUTTRANSAM-RXN|reaction.ecocyc.PUTTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3901|reaction.ecocyc.RXN0-3901]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SPERMIDINESYN-RXN|reaction.ecocyc.SPERMIDINESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-328|reaction.ecocyc.TRANS-RXN-328]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-69|reaction.ecocyc.TRANS-RXN-69]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-211|reaction.ecocyc.TRANS-RXN0-211]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.AGMATIN-RXN|reaction.ecocyc.AGMATIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LYSDECARBOX-RXN|reaction.ecocyc.LYSDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-2481|reaction.ecocyc.RXN0-2481]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (4)

- `transports` <-- [[complex.ecocyc.ABC-24-CPLX|complex.ecocyc.ABC-24-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-13226|complex.ecocyc.CPLX0-13226]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AA47|protein.P0AA47]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AAF1|protein.P0AAF1]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00134`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
