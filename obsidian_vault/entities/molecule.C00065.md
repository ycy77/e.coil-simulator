---
entity_id: "molecule.C00065"
entity_type: "small_molecule"
name: "L-Serine"
source_database: "KEGG"
source_id: "C00065"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Serine"
  - "L-2-Amino-3-hydroxypropionic acid"
  - "L-3-Hydroxy-alanine"
  - "Serine"
---

# L-Serine

`molecule.C00065`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00065`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Serine; L-2-Amino-3-hydroxypropionic acid; L-3-Hydroxy-alanine; Serine

## Biological Role

Consumed as substrate in 26 reaction(s). Produced in 12 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Serine; L-2-Amino-3-hydroxypropionic acid; L-3-Hydroxy-alanine; Serine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (46)

- `is_product_of` --> [[reaction.R00582|reaction.R00582]] `KEGG` `database` - C01005 + C00001 <=> C00065 + C00009
- `is_product_of` --> [[reaction.ecocyc.GLYOHMETRANS-RXN|reaction.ecocyc.GLYOHMETRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14136|reaction.ecocyc.RXN-14136]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-23948|reaction.ecocyc.RXN-23948]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-23961|reaction.ecocyc.RXN-23961]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-25001|reaction.ecocyc.RXN-25001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-4083|reaction.ecocyc.RXN0-4083]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5114|reaction.ecocyc.RXN0-5114]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7432|reaction.ecocyc.RXN0-7432]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7433|reaction.ecocyc.RXN0-7433]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7435|reaction.ecocyc.RXN0-7435]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-71|reaction.ecocyc.TRANS-RXN-71]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00220|reaction.R00220]] `KEGG` `database` - C00065 <=> C00022 + C00014
- `is_substrate_of` --> [[reaction.R00586|reaction.R00586]] `KEGG` `database` - C00065 + C00024 <=> C00979 + C00010
- `is_substrate_of` --> [[reaction.R00589|reaction.R00589]] `KEGG` `database` - C00065 <=> C00740
- `is_substrate_of` --> [[reaction.R00590|reaction.R00590]] `KEGG` `database` - C00065 <=> C02218 + C00001
- `is_substrate_of` --> [[reaction.R00674|reaction.R00674]] `KEGG` `database` - C00065 + C00463 <=> C00078 + C00001
- `is_substrate_of` --> [[reaction.R03662|reaction.R03662]] `KEGG` `database` - C00002 + C00065 + C01650 <=> C00020 + C00013 + C02553
- `is_substrate_of` --> [[reaction.R08218|reaction.R08218]] `KEGG` `database` - C00002 + C00065 + C16636 <=> C00020 + C00013 + C06481
- `is_substrate_of` --> [[reaction.R09099|reaction.R09099]] `KEGG` `database` - C00065 + C01217 <=> C04377 + C00037 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.4.3.1.17-RXN|reaction.ecocyc.4.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ENTF-RXN|reaction.ecocyc.ENTF-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ENTMULTI-RXN|reaction.ecocyc.ENTMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHOSPHASERSYN-RXN|reaction.ecocyc.PHOSPHASERSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15125|reaction.ecocyc.RXN-15125]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16003|reaction.ecocyc.RXN-16003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19472|reaction.ecocyc.RXN-19472]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19474|reaction.ecocyc.RXN-19474]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23947|reaction.ecocyc.RXN-23947]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23960|reaction.ecocyc.RXN-23960]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2161|reaction.ecocyc.RXN0-2161]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2201|reaction.ecocyc.RXN0-2201]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2382|reaction.ecocyc.RXN0-2382]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4083|reaction.ecocyc.RXN0-4083]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SERINE--TRNA-LIGASE-RXN|reaction.ecocyc.SERINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SERINE-O-ACETTRAN-RXN|reaction.ecocyc.SERINE-O-ACETTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-71|reaction.ecocyc.TRANS-RXN-71]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRYPSYN-RXN|reaction.ecocyc.TRYPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DSERDEAM-RXN|reaction.ecocyc.DSERDEAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTAMINESYN-RXN|reaction.ecocyc.GLUTAMINESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KETOGLUTREDUCT-RXN|reaction.ecocyc.KETOGLUTREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PGLYCDEHYDROG-RXN|reaction.ecocyc.PGLYCDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-16701|reaction.ecocyc.RXN-16701]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5114|reaction.ecocyc.RXN0-5114]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SERINE-O-ACETTRAN-RXN|reaction.ecocyc.SERINE-O-ACETTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-469|reaction.ecocyc.TRANS-RXN0-469]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (3)

- `transports` <-- [[protein.P0AAD8|protein.P0AAD8]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AGE4|protein.P0AGE4]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P75712|protein.P75712]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00065`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
