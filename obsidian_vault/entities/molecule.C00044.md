---
entity_id: "molecule.C00044"
entity_type: "small_molecule"
name: "GTP"
source_database: "KEGG"
source_id: "C00044"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "GTP"
  - "Guanosine 5'-triphosphate"
---

# GTP

`molecule.C00044`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00044`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: GTP; Guanosine 5'-triphosphate

## Biological Role

Consumed as substrate in 38 reaction(s). Produced in 3 reaction(s). Binds McrBC restriction endonuclease (complex.ecocyc.CPLX0-2661).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

KEGG compound: GTP; Guanosine 5'-triphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (62)

- `activates` --> [[reaction.ecocyc.CTPSYN-RXN|reaction.ecocyc.CTPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN-12002|reaction.ecocyc.RXN-12002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN|reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `binds` --> [[complex.ecocyc.CPLX0-2661|complex.ecocyc.CPLX0-2661]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.R00330|reaction.R00330]] `KEGG` `database` - C00002 + C00035 <=> C00008 + C00044
- `is_product_of` --> [[reaction.ecocyc.GDPKIN-RXN|reaction.ecocyc.GDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6427|reaction.ecocyc.RXN0-6427]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00335|reaction.R00335]] `KEGG` `database` - C00044 + C00001 <=> C00035 + C00009
- `is_substrate_of` --> [[reaction.R00424|reaction.R00424]] `KEGG` `database` - C00044 + C00001 <=> C04895 + C00058
- `is_substrate_of` --> [[reaction.R00425|reaction.R00425]] `KEGG` `database` - C00044 + 4 C00001 <=> C00058 + C01304 + 2 C00009
- `is_substrate_of` --> [[reaction.R00426|reaction.R00426]] `KEGG` `database` - C00044 + C00001 <=> C00144 + C00013
- `is_substrate_of` --> [[reaction.R00428|reaction.R00428]] `KEGG` `database` - C00044 + C00001 <=> C05922
- `is_substrate_of` --> [[reaction.R00429|reaction.R00429]] `KEGG` `database` - C00002 + C00044 <=> C00020 + C04494
- `is_substrate_of` --> [[reaction.R00430|reaction.R00430]] `KEGG` `database` - C00044 + C00022 <=> C00035 + C00074
- `is_substrate_of` --> [[reaction.R00434|reaction.R00434]] `KEGG` `database` - C00044 <=> C00942 + C00013
- `is_substrate_of` --> [[reaction.R00441|reaction.R00441]] `KEGG` `database` - C00044 + C00046 <=> C00013 + C00046
- `is_substrate_of` --> [[reaction.R00517|reaction.R00517]] `KEGG` `database` - C00044 + C00475 <=> C00035 + C00055
- `is_substrate_of` --> [[reaction.R01135|reaction.R01135]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_substrate_of` --> [[reaction.ecocyc.2.7.7.13-RXN|reaction.ecocyc.2.7.7.13-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN|reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.COBINPGUANYLYLTRANS-RXN|reaction.ecocyc.COBINPGUANYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CYTIDINEKIN-RXN|reaction.ecocyc.CYTIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GTPPYPHOSKIN-RXN|reaction.ecocyc.GTPPYPHOSKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GUANYLCYC-RXN|reaction.ecocyc.GUANYLCYC-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11409|reaction.ecocyc.RXN-11409]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14074|reaction.ecocyc.RXN-14074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16456|reaction.ecocyc.RXN-16456]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17905|reaction.ecocyc.RXN-17905]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17935|reaction.ecocyc.RXN-17935]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18710|reaction.ecocyc.RXN-18710]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21601|reaction.ecocyc.RXN-21601]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22956|reaction.ecocyc.RXN-22956]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8340|reaction.ecocyc.RXN-8340]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-262|reaction.ecocyc.RXN0-262]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2941|reaction.ecocyc.RXN0-2941]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6566|reaction.ecocyc.RXN0-6566]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7068|reaction.ecocyc.RXN0-7068]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7083|reaction.ecocyc.RXN0-7083]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-746|reaction.ecocyc.RXN0-746]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-424|reaction.ecocyc.TRANS-RXN-424]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.URKI-RXN|reaction.ecocyc.URKI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3.6.1.41-RXN|reaction.ecocyc.3.6.1.41-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.6PFRUCTPHOS-RXN|reaction.ecocyc.6PFRUCTPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ADENYLATECYC-RXN|reaction.ecocyc.ADENYLATECYC-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CTPSYN-RXN|reaction.ecocyc.CTPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DGTPTRIPHYDRO-RXN|reaction.ecocyc.DGTPTRIPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GUANOSINEKIN-RXN|reaction.ecocyc.GUANOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GUANYL-KIN-RXN|reaction.ecocyc.GUANYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN|reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.NUCLEOSIDE-DIP-KIN-RXN|reaction.ecocyc.NUCLEOSIDE-DIP-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSPHOGLUCMUT-RXN|reaction.ecocyc.PHOSPHOGLUCMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5073|reaction.ecocyc.RXN0-5073]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7079|reaction.ecocyc.RXN0-7079]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THI-P-SYN-RXN|reaction.ecocyc.THI-P-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P33650|protein.P33650]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00044`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
