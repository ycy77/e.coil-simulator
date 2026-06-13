---
entity_id: "complex.ecocyc.CPLX0-7609"
entity_type: "complex"
name: "5-carboxymethylaminomethyluridine-tRNA synthase [multifunctional]"
source_database: "EcoCyc"
source_id: "CPLX0-7609"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 5-carboxymethylaminomethyluridine-tRNA synthase [multifunctional]

`complex.ecocyc.CPLX0-7609`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7609`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7608|complex.ecocyc.CPLX0-7608]], [[complex.ecocyc.CPLX0-7597|complex.ecocyc.CPLX0-7597]]

## Enriched Summary

The MnmEG complex is required for 5-carboxymethylaminomethyl modification of the wobble base of certain tRNAs. Both complex formation and GTP hydrolysis are required for tRNA modification activity . The interaction between MnmE, MnmG and tRNA as well as associated conformational changes were studied by small-angle X-ray scattering (SAXS). Binding of GTP leads to the formation of an MnmE4MnmG2 complex from MnmE2MnmG2 . Utilizing either ammonium or glycine as a substrate, the MnmEG complex catalyzes formation of the 5-aminomethyl- or 5-carboxymethylaminomethyl modification of tRNA at the U34 wobble base . All its tRNA substrates can be modified via the ammonium pathway; growth conditions influence which modification pathway is utilized . Thiolation of the C2 position (catalyzed by MnmA) and modification of the C5 position of U34 are independent of each other. Reviews: The MnmEG complex is required for 5-carboxymethylaminomethyl modification of the wobble base of certain tRNAs. Both complex formation and GTP hydrolysis are required for tRNA modification activity . The interaction between MnmE, MnmG and tRNA as well as associated conformational changes were studied by small-angle X-ray scattering (SAXS). Binding of GTP leads to the formation of an MnmE4MnmG2 complex from MnmE2MnmG2...

## Biological Role

Catalyzes RXN-18710 (reaction.ecocyc.RXN-18710), RXN0-7068 (reaction.ecocyc.RXN0-7068), RXN0-7083 (reaction.ecocyc.RXN0-7083). Bound by FAD (molecule.C00016).

## Annotation

The MnmEG complex is required for 5-carboxymethylaminomethyl modification of the wobble base of certain tRNAs. Both complex formation and GTP hydrolysis are required for tRNA modification activity . The interaction between MnmE, MnmG and tRNA as well as associated conformational changes were studied by small-angle X-ray scattering (SAXS). Binding of GTP leads to the formation of an MnmE4MnmG2 complex from MnmE2MnmG2 . Utilizing either ammonium or glycine as a substrate, the MnmEG complex catalyzes formation of the 5-aminomethyl- or 5-carboxymethylaminomethyl modification of tRNA at the U34 wobble base . All its tRNA substrates can be modified via the ammonium pathway; growth conditions influence which modification pathway is utilized . Thiolation of the C2 position (catalyzed by MnmA) and modification of the C5 position of U34 are independent of each other. Reviews:

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-18710|reaction.ecocyc.RXN-18710]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7068|reaction.ecocyc.RXN0-7068]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7083|reaction.ecocyc.RXN0-7083]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.CPLX0-7597|complex.ecocyc.CPLX0-7597]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CPLX0-7608|complex.ecocyc.CPLX0-7608]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A6U3|protein.P0A6U3]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P25522|protein.P25522]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7609`
- `QSPROTEOME:QS00186945`

## Notes

1*complex.ecocyc.CPLX0-7608|1*complex.ecocyc.CPLX0-7597
