---
entity_id: "molecule.C00082"
entity_type: "small_molecule"
name: "L-Tyrosine"
source_database: "KEGG"
source_id: "C00082"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Tyrosine"
  - "(S)-3-(p-Hydroxyphenyl)alanine"
  - "(S)-2-Amino-3-(p-hydroxyphenyl)propionic acid"
  - "Tyrosine"
---

# L-Tyrosine

`molecule.C00082`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00082`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Tyrosine; (S)-3-(p-Hydroxyphenyl)alanine; (S)-2-Amino-3-(p-hydroxyphenyl)propionic acid; Tyrosine

## Biological Role

Consumed as substrate in 11 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: L-Tyrosine; (S)-3-(p-Hydroxyphenyl)alanine; (S)-2-Amino-3-(p-hydroxyphenyl)propionic acid; Tyrosine

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (21)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-162|complex.ecocyc.MONOMER0-162]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN-14534|reaction.ecocyc.RXN-14534]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-23958|reaction.ecocyc.RXN-23958]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-77|reaction.ecocyc.TRANS-RXN-77]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00734|reaction.R00734]] `KEGG` `database` - C00082 + C00026 <=> C01179 + C00025
- `is_substrate_of` --> [[reaction.R02918|reaction.R02918]] `KEGG` `database` - C00002 + C00082 + C00787 <=> C00020 + C00013 + C02839
- `is_substrate_of` --> [[reaction.R10246|reaction.R10246]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11319|reaction.ecocyc.RXN-11319]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23088|reaction.ecocyc.RXN-23088]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23957|reaction.ecocyc.RXN-23957]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8487|reaction.ecocyc.RXN-8487]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-296|reaction.ecocyc.RXN0-296]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-77|reaction.ecocyc.TRANS-RXN-77]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TYROSINE--TRNA-LIGASE-RXN|reaction.ecocyc.TYROSINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CHORISMATEMUT-RXN|reaction.ecocyc.CHORISMATEMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PREPHENATEDEHYDROG-RXN|reaction.ecocyc.PREPHENATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AAD4|protein.P0AAD4]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00082`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
