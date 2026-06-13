---
entity_id: "complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX"
entity_type: "complex"
name: "ribonucleoside-diphosphate reductase 2"
source_database: "EcoCyc"
source_id: "RIBONUCLEOSIDE-DIP-REDUCTII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "RDPR-II"
---

# ribonucleoside-diphosphate reductase 2

`complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RIBONUCLEOSIDE-DIP-REDUCTII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.NRDE-CPLX|complex.ecocyc.NRDE-CPLX]], [[complex.ecocyc.NRDF-CPLX|complex.ecocyc.NRDF-CPLX]]

## Enriched Summary

The NrdE and NrdF proteins constitute a second class I ribonucleotide reductase (RDPR-II) in E. coli, converting nucleoside 5'-diphosphates to deoxynucleoside 5'-diphosphates. The enzyme belongs to the class Ib ribonucleotide reductases that are active under aerobic conditions. Recently, it was shown that RDPR-II is active under conditions of iron starvation, when the housekeeping enzyme RDPR-I (NrdAB) is not active . The catalytic mechanism involves a tyrosyl radical at the active site that inititates ribonucleotide reduction. The nature of the metal ion cofactor for NrdF has been controversial, but recent results show that the MnIII2-Y· form is the active form of NrdF and is generated from two HO2- anions supplied by G7402-MONOMER "NrdI" . Crystal structures of MnII2-NrdF with reduced or oxidized NrdI show a channel connecting the flavin cofactor of NrdI to the NrdF active site . The glutaredoxin-like protein G7401-MONOMER "NrdH" apparently replaces thioredoxin as the electron donor for ribonucleotide reduction . RDPR-II is an aerobic enzyme that is not essential for growth . It cannot support aerobic or microaerophilic growth in an nrdAB deletion mutant. However, overexpression of nrdHIEF can rescue the growth defect of the nrdAB mutant . Expression of the nrdHIEF operon is increased by hydroxyurea and oxidative stress...

## Biological Role

Catalyzes RIBONUCLEOSIDE-DIP-REDUCTI-RXN (reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN), RIBONUCLEOSIDE-DIP-REDUCTII-RXN (reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-RXN), RXN0-722 (reaction.ecocyc.RXN0-722), RXN0-747 (reaction.ecocyc.RXN0-747), RXN0-748 (reaction.ecocyc.RXN0-748).

## Annotation

The NrdE and NrdF proteins constitute a second class I ribonucleotide reductase (RDPR-II) in E. coli, converting nucleoside 5'-diphosphates to deoxynucleoside 5'-diphosphates. The enzyme belongs to the class Ib ribonucleotide reductases that are active under aerobic conditions. Recently, it was shown that RDPR-II is active under conditions of iron starvation, when the housekeeping enzyme RDPR-I (NrdAB) is not active . The catalytic mechanism involves a tyrosyl radical at the active site that inititates ribonucleotide reduction. The nature of the metal ion cofactor for NrdF has been controversial, but recent results show that the MnIII2-Y· form is the active form of NrdF and is generated from two HO2- anions supplied by G7402-MONOMER "NrdI" . Crystal structures of MnII2-NrdF with reduced or oxidized NrdI show a channel connecting the flavin cofactor of NrdI to the NrdF active site . The glutaredoxin-like protein G7401-MONOMER "NrdH" apparently replaces thioredoxin as the electron donor for ribonucleotide reduction . RDPR-II is an aerobic enzyme that is not essential for growth . It cannot support aerobic or microaerophilic growth in an nrdAB deletion mutant. However, overexpression of nrdHIEF can rescue the growth defect of the nrdAB mutant . Expression of the nrdHIEF operon is increased by hydroxyurea and oxidative stress . Expression is highest in minimal medium and in early log phase growth in complex medium; deletion of Trx1 and Grx1 (trxA- grxA-) increases expression more than 100-fold . nrdHIEF belongs to the Fur regulon . An nrdEF mutant is viable under both aerobic and anaerobic conditions . Reviews:

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN|reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-RXN|reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-722|reaction.ecocyc.RXN0-722]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-747|reaction.ecocyc.RXN0-747]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-748|reaction.ecocyc.RXN0-748]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.NRDE-CPLX|complex.ecocyc.NRDE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.NRDF-CPLX|complex.ecocyc.NRDF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P37146|protein.P37146]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P39452|protein.P39452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:RIBONUCLEOSIDE-DIP-REDUCTII-CPLX`
- `QSPROTEOME:QS00198767`

## Notes

1*complex.ecocyc.NRDE-CPLX|1*complex.ecocyc.NRDF-CPLX
