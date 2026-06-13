---
entity_id: "molecule.C00073"
entity_type: "small_molecule"
name: "L-Methionine"
source_database: "KEGG"
source_id: "C00073"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Methionine"
  - "Methionine"
  - "L-2-Amino-4methylthiobutyric acid"
---

# L-Methionine

`molecule.C00073`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00073`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Methionine; Methionine; L-2-Amino-4methylthiobutyric acid MET (met) is one of the proteinogenic amino acids. In addition to its role in proteins, L-methionine is required for a number of important cellular functions, including the initiation of protein synthesis, the methylation of DNA, rRNA and xenobiotics, and the biosynthesis of cysteine, phospholipids and polyamines. In all metzoa MET is an essential amino acid (an indispensable amino acid that cannot be synthesized de novo) and must be supplied in the diet.

## Biological Role

Consumed as substrate in 13 reaction(s). Produced in 35 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: L-Methionine; Methionine; L-2-Amino-4methylthiobutyric acid

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (53)

- `activates` --> [[reaction.ecocyc.FORMYLTHFDEFORMYL-RXN|reaction.ecocyc.FORMYLTHFDEFORMYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00177|reaction.R00177]] `KEGG` `database` - C00009 + C00013 + C00019 <=> C00002 + C00073 + C00001
- `is_product_of` --> [[reaction.R00650|reaction.R00650]] `KEGG` `database` - C00019 + C00155 <=> C00021 + C00073
- `is_product_of` --> [[reaction.R04405|reaction.R04405]] `KEGG` `database` - C04489 + C00155 <=> C04144 + C00073
- `is_product_of` --> [[reaction.R04710|reaction.R04710]] `KEGG` `database` - C00019 + C05196 + C05197 <=> C05198 + C00073 + C05199 + C05312
- `is_product_of` --> [[reaction.R06895|reaction.R06895]] `KEGG` `database` - C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198
- `is_product_of` --> [[reaction.R07767|reaction.R07767]] `KEGG` `database` - C16236 + C22154 + 2 C00019 + 2 C22150 + 8 C00080 <=> C16832 + C22155 + 2 C00283 + 4 C14818 + 2 C00073 + 2 C05198 + 2 C22151
- `is_product_of` --> [[reaction.R10220|reaction.R10220]] `KEGG` `database` - C00019 + C20446 <=> C00073 + C00147 + C19647
- `is_product_of` --> [[reaction.R10246|reaction.R10246]] `KEGG` `database` - C00082 + C00019 + C00030 <=> C15809 + C01468 + C05198 + C00073 + C00028
- `is_product_of` --> [[reaction.ecocyc.1.97.1.4-A-RXN|reaction.ecocyc.1.97.1.4-A-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.3.4.11.18-RXN|reaction.ecocyc.3.4.11.18-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HEMN-RXN|reaction.ecocyc.HEMN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HOMOCYSMET-RXN|reaction.ecocyc.HOMOCYSMET-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HOMOCYSMETB12-RXN|reaction.ecocyc.HOMOCYSMETB12-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN|reaction.ecocyc.HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MMUM-RXN|reaction.ecocyc.MMUM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYRIMSYN1-RXN|reaction.ecocyc.PYRIMSYN1-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RNTRACTIV-RXN|reaction.ecocyc.RNTRACTIV-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11319|reaction.ecocyc.RXN-11319]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11586|reaction.ecocyc.RXN-11586]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17473|reaction.ecocyc.RXN-17473]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17956|reaction.ecocyc.RXN-17956]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21538|reaction.ecocyc.RXN-21538]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-25170|reaction.ecocyc.RXN-25170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-25310|reaction.ecocyc.RXN-25310]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-8340|reaction.ecocyc.RXN-8340]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1342|reaction.ecocyc.RXN0-1342]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-4522|reaction.ecocyc.RXN0-4522]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5063|reaction.ecocyc.RXN0-5063]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6366|reaction.ecocyc.RXN0-6366]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6734|reaction.ecocyc.RXN0-6734]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6974|reaction.ecocyc.RXN0-6974]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6985|reaction.ecocyc.RXN0-6985]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7007|reaction.ecocyc.RXN0-7007]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7050|reaction.ecocyc.RXN0-7050]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-949|reaction.ecocyc.RXN0-949]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.1.8.4.13-RXN|reaction.ecocyc.1.8.4.13-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.8.4.14-RXN|reaction.ecocyc.1.8.4.14-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.METHIONINE--TRNA-LIGASE-RXN|reaction.ecocyc.METHIONINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R15-RXN|reaction.ecocyc.R15-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16165|reaction.ecocyc.RXN-16165]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23891|reaction.ecocyc.RXN-23891]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4522|reaction.ecocyc.RXN0-4522]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6721|reaction.ecocyc.RXN0-6721]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6948|reaction.ecocyc.RXN0-6948]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7050|reaction.ecocyc.RXN0-7050]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7187|reaction.ecocyc.RXN0-7187]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7188|reaction.ecocyc.RXN0-7188]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.S-ADENMETSYN-RXN|reaction.ecocyc.S-ADENMETSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTAMATESYN-RXN|reaction.ecocyc.GLUTAMATESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HOMSUCTRAN-RXN|reaction.ecocyc.HOMSUCTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-25310|reaction.ecocyc.RXN-25310]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-202|reaction.ecocyc.TRANS-RXN0-202]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX|complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P39277|protein.P39277]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00073`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
