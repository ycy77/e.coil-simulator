---
entity_id: "molecule.C00097"
entity_type: "small_molecule"
name: "L-Cysteine"
source_database: "KEGG"
source_id: "C00097"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Cysteine"
  - "L-2-Amino-3-mercaptopropionic acid"
---

# L-Cysteine

`molecule.C00097`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00097`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Cysteine; L-2-Amino-3-mercaptopropionic acid

## Biological Role

Consumed as substrate in 27 reaction(s). Produced in 10 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

KEGG compound: L-Cysteine; L-2-Amino-3-mercaptopropionic acid

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (51)

- `activates` --> [[reaction.ecocyc.PHOSPHOGLUCMUT-RXN|reaction.ecocyc.PHOSPHOGLUCMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R07274|reaction.R07274]] `KEGG` `database` - C01005 + C00283 <=> C00097 + C00009
- `is_product_of` --> [[reaction.ecocyc.1.8.4.4-RXN|reaction.ecocyc.1.8.4.4-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACSERLY-RXN|reaction.ecocyc.ACSERLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18586|reaction.ecocyc.RXN-18586]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19629|reaction.ecocyc.RXN-19629]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21077|reaction.ecocyc.RXN-21077]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-23966|reaction.ecocyc.RXN-23966]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-6622|reaction.ecocyc.RXN-6622]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1924|reaction.ecocyc.RXN0-1924]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3|reaction.ecocyc.RXN0-3]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00782|reaction.R00782]] `KEGG` `database` - C00097 + C00001 <=> C00283 + C00022 + C00014
- `is_substrate_of` --> [[reaction.R11528|reaction.R11528]] `KEGG` `database` - C00097 + C02743 <=> C00041 + C21440
- `is_substrate_of` --> [[reaction.ecocyc.CYSTEINE--TRNA-LIGASE-RXN|reaction.ecocyc.CYSTEINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTCYSLIG-RXN|reaction.ecocyc.GLUTCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN|reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.P-PANTOCYSLIG-RXN|reaction.ecocyc.P-PANTOCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11115|reaction.ecocyc.RXN-11115]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12588|reaction.ecocyc.RXN-12588]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15129|reaction.ecocyc.RXN-15129]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15881|reaction.ecocyc.RXN-15881]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21566|reaction.ecocyc.RXN-21566]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22606|reaction.ecocyc.RXN-22606]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22698|reaction.ecocyc.RXN-22698]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22700|reaction.ecocyc.RXN-22700]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22915|reaction.ecocyc.RXN-22915]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23942|reaction.ecocyc.RXN-23942]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23966|reaction.ecocyc.RXN-23966]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25085|reaction.ecocyc.RXN-25085]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9787|reaction.ecocyc.RXN-9787]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1924|reaction.ecocyc.RXN0-1924]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3|reaction.ecocyc.RXN0-3]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-308|reaction.ecocyc.RXN0-308]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6990|reaction.ecocyc.RXN0-6990]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7438|reaction.ecocyc.RXN0-7438]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7439|reaction.ecocyc.RXN0-7439]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.4.3.1.17-RXN|reaction.ecocyc.4.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.7KAPSYN-RXN|reaction.ecocyc.7KAPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.AKBLIG-RXN|reaction.ecocyc.AKBLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ALKAPHOSPHA-RXN|reaction.ecocyc.ALKAPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN|reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DCYSDESULF-RXN|reaction.ecocyc.DCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GALACTUROISOM-RXN|reaction.ecocyc.GALACTUROISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUCUROISOM-RXN|reaction.ecocyc.GLUCUROISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HOMOSERKIN-RXN|reaction.ecocyc.HOMOSERKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SERINE-O-ACETTRAN-RXN|reaction.ecocyc.SERINE-O-ACETTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN-285|reaction.ecocyc.TRANS-RXN-285]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-593|reaction.ecocyc.TRANS-RXN0-593]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-6-CPLX|complex.ecocyc.ABC-6-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00097`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
