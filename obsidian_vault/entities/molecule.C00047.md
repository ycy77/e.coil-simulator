---
entity_id: "molecule.C00047"
entity_type: "small_molecule"
name: "L-Lysine"
source_database: "KEGG"
source_id: "C00047"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Lysine"
  - "Lysine acid"
  - "2,6-Diaminohexanoic acid"
---

# L-Lysine

`molecule.C00047`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00047`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Lysine; Lysine acid; 2,6-Diaminohexanoic acid

## Biological Role

Consumed as substrate in 16 reaction(s). Produced in 8 reaction(s). Binds lysine—tRNA ligase (complex.ecocyc.LYSU-CPLX).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Lysine; Lysine acid; 2,6-Diaminohexanoic acid

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (31)

- `binds` --> [[complex.ecocyc.LYSU-CPLX|complex.ecocyc.LYSU-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` --> [[complex.ecocyc.CPLX0-7670|complex.ecocyc.CPLX0-7670]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00451|reaction.R00451]] `KEGG` `database` - C00680 <=> C00047 + C00011
- `is_product_of` --> [[reaction.ecocyc.ABC-3-RXN|reaction.ecocyc.ABC-3-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DIAMINOPIMDECARB-RXN|reaction.ecocyc.DIAMINOPIMDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-963|reaction.ecocyc.RXN0-963]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-401|reaction.ecocyc.TRANS-RXN-401]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-58|reaction.ecocyc.TRANS-RXN-58]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-68|reaction.ecocyc.TRANS-RXN-68]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-569|reaction.ecocyc.TRANS-RXN0-569]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00460|reaction.R00460]] `KEGG` `database` - C00047 <=> C00739
- `is_substrate_of` --> [[reaction.R00462|reaction.R00462]] `KEGG` `database` - C00047 <=> C01672 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.ABC-3-RXN|reaction.ecocyc.ABC-3-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.LYSDECARBOX-RXN|reaction.ecocyc.LYSDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN|reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-1961|reaction.ecocyc.RXN-1961]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20898|reaction.ecocyc.RXN-20898]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20900|reaction.ecocyc.RXN-20900]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22679|reaction.ecocyc.RXN-22679]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22777|reaction.ecocyc.RXN-22777]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5192|reaction.ecocyc.RXN0-5192]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5344|reaction.ecocyc.RXN0-5344]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-401|reaction.ecocyc.TRANS-RXN-401]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-58|reaction.ecocyc.TRANS-RXN-58]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-68|reaction.ecocyc.TRANS-RXN-68]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-569|reaction.ecocyc.TRANS-RXN0-569]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ASPARTATEKIN-RXN|reaction.ecocyc.ASPARTATEKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DIAMINOPIMDECARB-RXN|reaction.ecocyc.DIAMINOPIMDECARB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DIHYDRODIPICSYN-RXN|reaction.ecocyc.DIHYDRODIPICSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HOMOSERKIN-RXN|reaction.ecocyc.HOMOSERKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (4)

- `transports` <-- [[complex.ecocyc.ABC-3-CPLX|complex.ecocyc.ABC-3-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AAE8|protein.P0AAE8]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P25737|protein.P25737]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P75826|protein.P75826]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00047`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
