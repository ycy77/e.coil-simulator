---
entity_id: "complex.ecocyc.CPLX0-1923"
entity_type: "complex"
name: "energy transducing Ton complex"
source_database: "EcoCyc"
source_id: "CPLX0-1923"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# energy transducing Ton complex

`complex.ecocyc.CPLX0-1923`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1923`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P02929|protein.P02929]], [[protein.P0ABU7|protein.P0ABU7]], [[protein.P0ABV2|protein.P0ABV2]]

## Enriched Summary

In E. coli K-12 the Ton system functions to transduce the energy of the proton motive force (pmf) at the cytoplasmic membrane to ligand-specific outer membrane transporters to support the active transport of iron-siderophore complexes and vitamin B12 across the outer membrane. The Ton system consists of 3 inner membrane proteins - TonB, ExbB and ExbD (the Ton complex) - which mediate energy transfer to the outer membrane transporters for iron siderophores (FepA, FecA, FhuA, FhuE, Fiu, and CirA) and cofactors (BtuB, PqqU). Ton system proteins are consistently present in a ratio of 1:7:2 (TonB:ExbB:ExbD) . Purified, reconstituted Ton complex has a stoichiometry of 1:4:1 (TonB:ExbB:ExbD) . The Ton complex consists of a pentamer of ExbB, a dimer of ExbD and at least one TonB . ExbBD is a heteroheptameric 5:2 rotary motor (see ). Energy transduction was initially thought to occur through a shuttling mechanism whereby TonB physically moved between membranes to release conformationally stored potential energy (reviewed in ). Later experiments disproved the shuttle idea (reviewed in ) and several other models have since been advanced . TonB action has also been described by a rotational surveillance and energy transfer (ROSET) model (reviewed in )...

## Biological Role

Component of cobalamin outer membrane transport complex (complex.ecocyc.CPLX0-1924), ferric enterobactin outer membrane transport complex (complex.ecocyc.CPLX0-1941), ferrichrome outer membrane transport complex (complex.ecocyc.CPLX0-1942), ferric citrate outer membrane transport complex (complex.ecocyc.CPLX0-1943), ferric coprogen outer membrane transport complex (complex.ecocyc.CPLX0-7952), ferric catecholate outer membrane transport complex I (complex.ecocyc.CPLX0-8541), ferric catecholate outer membrane transport complex II (complex.ecocyc.CPLX0-8553), pyrroloquinoline quinone outer membrane transport complex (complex.ecocyc.CPLX0-9372).

## Annotation

In E. coli K-12 the Ton system functions to transduce the energy of the proton motive force (pmf) at the cytoplasmic membrane to ligand-specific outer membrane transporters to support the active transport of iron-siderophore complexes and vitamin B12 across the outer membrane. The Ton system consists of 3 inner membrane proteins - TonB, ExbB and ExbD (the Ton complex) - which mediate energy transfer to the outer membrane transporters for iron siderophores (FepA, FecA, FhuA, FhuE, Fiu, and CirA) and cofactors (BtuB, PqqU). Ton system proteins are consistently present in a ratio of 1:7:2 (TonB:ExbB:ExbD) . Purified, reconstituted Ton complex has a stoichiometry of 1:4:1 (TonB:ExbB:ExbD) . The Ton complex consists of a pentamer of ExbB, a dimer of ExbD and at least one TonB . ExbBD is a heteroheptameric 5:2 rotary motor (see ). Energy transduction was initially thought to occur through a shuttling mechanism whereby TonB physically moved between membranes to release conformationally stored potential energy (reviewed in ). Later experiments disproved the shuttle idea (reviewed in ) and several other models have since been advanced . TonB action has also been described by a rotational surveillance and energy transfer (ROSET) model (reviewed in ). In this model PMF-driven rotation of TonB and ExbB promotes lateral movement of the complex through the inner membrane and hence movement of the C-terminal domain of TonB along the periplasmic face of the OM; after encountering and binding an exposed Ton box of a ligand bound transporter, the kinetic energy from TonB rotation is transferred to create conformational motion in the OM transporter. TonB-ExbB-ExbD and TolA-TolQ-TolR (of the CPLX0-2201) may be analogous systems of energy transduction Reviews:

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-1941|complex.ecocyc.CPLX0-1941]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-1942|complex.ecocyc.CPLX0-1942]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-1943|complex.ecocyc.CPLX0-1943]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7952|complex.ecocyc.CPLX0-7952]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8541|complex.ecocyc.CPLX0-8541]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8553|complex.ecocyc.CPLX0-8553]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-9372|complex.ecocyc.CPLX0-9372]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P02929|protein.P02929]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABU7|protein.P0ABU7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=5
- `is_component_of` <-- [[protein.P0ABV2|protein.P0ABV2]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-1923`
- `PDB:8VGC`
- `PDB:8VGD`
- `PDB:9DDQ`
- `PDB:9DDP`
- `PDB:9DDO`
- `QSPROTEOME:QS00049414`

## Notes

5*protein.P02929|2*protein.P0ABU7|protein.P0ABV2
