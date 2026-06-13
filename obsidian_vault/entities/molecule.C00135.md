---
entity_id: "molecule.C00135"
entity_type: "small_molecule"
name: "L-Histidine"
source_database: "KEGG"
source_id: "C00135"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Histidine"
  - "(S)-alpha-Amino-1H-imidazole-4-propionic acid"
---

# L-Histidine

`molecule.C00135`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00135`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Histidine; (S)-alpha-Amino-1H-imidazole-4-propionic acid About the nomenclature of histidine: In the past two different systems of numbering the atoms in the imidazole ring of histidine had been used (biochemists numbering the nitrogen atom adjacent to the side chain as 1, while organic chemists designating it as 3), leading to considerable confusion. To avoid this confusion, IUPAC recommends to denote the nitrogen atoms of the imidazole ring of histidine by pros ('near', abbreviated π) and tele ('far', abbreviated τ) to show their position relative to the side chain. The carbon atom between the two ring nitrogen atoms is numbered 2 (as in imidazole), and the carbon atom next to the τ nitrogen is numbered 5. The carbon atoms of the aliphatic chain are designated α and β.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Histidine; (S)-alpha-Amino-1H-imidazole-4-propionic acid

## Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (12)

- `is_product_of` --> [[reaction.R01158|reaction.R01158]] `KEGG` `database` - C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080
- `is_product_of` --> [[reaction.R01163|reaction.R01163]] `KEGG` `database` - C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.ABC-14-RXN|reaction.ecocyc.ABC-14-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HISTALDEHYD-RXN|reaction.ecocyc.HISTALDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-8001|reaction.ecocyc.RXN-8001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6978|reaction.ecocyc.RXN0-6978]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-14-RXN|reaction.ecocyc.ABC-14-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HISTIDINE--TRNA-LIGASE-RXN|reaction.ecocyc.HISTIDINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23888|reaction.ecocyc.RXN-23888]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN|reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTAMINESYN-RXN|reaction.ecocyc.GLUTAMINESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HISTIDPHOS-RXN|reaction.ecocyc.HISTIDPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-14-CPLX|complex.ecocyc.ABC-14-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00135`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
