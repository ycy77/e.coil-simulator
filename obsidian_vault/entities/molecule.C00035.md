---
entity_id: "molecule.C00035"
entity_type: "small_molecule"
name: "GDP"
source_database: "KEGG"
source_id: "C00035"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "GDP"
  - "Guanosine 5'-diphosphate"
  - "Guanosine diphosphate"
---

# GDP

`molecule.C00035`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00035`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: GDP; Guanosine 5'-diphosphate; Guanosine diphosphate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 26 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: GDP; Guanosine 5'-diphosphate; Guanosine diphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (44)

- `activates` --> [[reaction.ecocyc.6PFRUCTPHOS-RXN|reaction.ecocyc.6PFRUCTPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00332|reaction.R00332]] `KEGG` `database` - C00002 + C00144 <=> C00008 + C00035
- `is_product_of` --> [[reaction.R00335|reaction.R00335]] `KEGG` `database` - C00044 + C00001 <=> C00035 + C00009
- `is_product_of` --> [[reaction.R00336|reaction.R00336]] `KEGG` `database` - C01228 + C00001 <=> C00035 + C00013
- `is_product_of` --> [[reaction.R00430|reaction.R00430]] `KEGG` `database` - C00044 + C00022 <=> C00035 + C00074
- `is_product_of` --> [[reaction.R00439|reaction.R00439]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00035
- `is_product_of` --> [[reaction.R00517|reaction.R00517]] `KEGG` `database` - C00044 + C00475 <=> C00035 + C00055
- `is_product_of` --> [[reaction.R01135|reaction.R01135]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_product_of` --> [[reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN|reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CYTIDINEKIN-RXN|reaction.ecocyc.CYTIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GDP-GLUCOSIDASE-RXN|reaction.ecocyc.GDP-GLUCOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GDPMANMANHYDRO-RXN|reaction.ecocyc.GDPMANMANHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GDPREDUCT-RXN|reaction.ecocyc.GDPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GUANYL-KIN-RXN|reaction.ecocyc.GUANYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PPGPPSYN-RXN|reaction.ecocyc.PPGPPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14074|reaction.ecocyc.RXN-14074]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18710|reaction.ecocyc.RXN-18710]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22956|reaction.ecocyc.RXN-22956]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2941|reaction.ecocyc.RXN0-2941]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7068|reaction.ecocyc.RXN0-7068]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7083|reaction.ecocyc.RXN0-7083]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7341|reaction.ecocyc.RXN0-7341]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7343|reaction.ecocyc.RXN0-7343]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-748|reaction.ecocyc.RXN0-748]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-424|reaction.ecocyc.TRANS-RXN-424]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URKI-RXN|reaction.ecocyc.URKI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00330|reaction.R00330]] `KEGG` `database` - C00002 + C00035 <=> C00008 + C00044
- `is_substrate_of` --> [[reaction.ecocyc.GDPKIN-RXN|reaction.ecocyc.GDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GDPPYPHOSKIN-RXN|reaction.ecocyc.GDPPYPHOSKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GUANOSINE-DIPHOSPHATASE-RXN|reaction.ecocyc.GUANOSINE-DIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.1.1.271-RXN|reaction.ecocyc.1.1.1.271-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DGTPTRIPHYDRO-RXN|reaction.ecocyc.DGTPTRIPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GDPMANMANHYDRO-RXN|reaction.ecocyc.GDPMANMANHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GUANOSINEKIN-RXN|reaction.ecocyc.GUANOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GUANYL-KIN-RXN|reaction.ecocyc.GUANYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.NUCLEOSIDE-DIP-KIN-RXN|reaction.ecocyc.NUCLEOSIDE-DIP-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PRPPAMIDOTRANS-RXN|reaction.ecocyc.PRPPAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5510|reaction.ecocyc.RXN0-5510]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7283|reaction.ecocyc.RXN0-7283]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P33650|protein.P33650]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00035`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
