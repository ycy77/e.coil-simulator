---
entity_id: "complex.ecocyc.ATPSYN-CPLX"
entity_type: "complex"
name: "ATP synthase / thiamin triphosphate synthase"
source_database: "EcoCyc"
source_id: "ATPSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "F<sub>o</sub>F<sub>1</sub>-ATP synthase"
  - "F<sub>1</sub>F<sub>o</sub>-ATP synthase"
  - "F<sub>o</sub>F<sub>1</sub> ATPase"
  - "F<sub>1</sub>F<sub>o</sub> ATPase"
---

# ATP synthase / thiamin triphosphate synthase

`complex.ecocyc.ATPSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ATPSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.F-O-CPLX|complex.ecocyc.F-O-CPLX]], [[complex.ecocyc.F-1-CPLX|complex.ecocyc.F-1-CPLX]]

## Enriched Summary

ATP synthase (also known as F1Fo synthase) catalyzes the synthesis of ATP from ADP and inorganic phosphate (Pi) under aerobic and anaerobic cell growth. ATP synthase uses the free energy derived from the transmembrane proton gradient to drive ATP synthesis (see review by and references therein). During fermentation ATP synthase functions in the reverse direction and catalyzes the hydrolysis of ATP to generate the electrochemical proton gradient needed for other membrane functions (see review by and references therein). ATP synthase is a rotary molecular nanomotor that couples the mechanical force of subunit rotation to the synthesis or hydrolysis of ATP at the enzyme's catalytic sites. Proton movement across the membrane generates subunit rotation which drives ATP synthesis by forcing sequential conformation change at each of the three catalytic sites. ATP synthase is comprised of two subcomplexes known as F1 and Fo (see review by and references therein). The hydrophilic F1 complex consists of five subunits (α, β, γ, δ and ε) in a stoichiometry of 3:3:1:1:1. The F1 complex contains three catalytic sites located in the three α/β subunit pairs. The Fo complex is membrane-embedded and forms the proton channel through the membrane. This complex consists of three subunits (a, b and c) in a stoichiometry of 1:2:10...

## Biological Role

Catalyzes ATPSYN-RXN (reaction.ecocyc.ATPSYN-RXN), RXN0-7041 (reaction.ecocyc.RXN0-7041). Transports Thiamin diphosphate (molecule.C00068), Thiamin triphosphate (molecule.C03028). Bound by Magnesium cation (molecule.C00305).

## Annotation

ATP synthase (also known as F1Fo synthase) catalyzes the synthesis of ATP from ADP and inorganic phosphate (Pi) under aerobic and anaerobic cell growth. ATP synthase uses the free energy derived from the transmembrane proton gradient to drive ATP synthesis (see review by and references therein). During fermentation ATP synthase functions in the reverse direction and catalyzes the hydrolysis of ATP to generate the electrochemical proton gradient needed for other membrane functions (see review by and references therein). ATP synthase is a rotary molecular nanomotor that couples the mechanical force of subunit rotation to the synthesis or hydrolysis of ATP at the enzyme's catalytic sites. Proton movement across the membrane generates subunit rotation which drives ATP synthesis by forcing sequential conformation change at each of the three catalytic sites. ATP synthase is comprised of two subcomplexes known as F1 and Fo (see review by and references therein). The hydrophilic F1 complex consists of five subunits (α, β, γ, δ and ε) in a stoichiometry of 3:3:1:1:1. The F1 complex contains three catalytic sites located in the three α/β subunit pairs. The Fo complex is membrane-embedded and forms the proton channel through the membrane. This complex consists of three subunits (a, b and c) in a stoichiometry of 1:2:10. Functionally, ATP synthase may be considered tripartite, consisting of a rotor (γεc10), a rotor stalk or stator (b2δ) and three catalytic sites (α3β3) where ATP synthesis or hydrolysis occurs (see review by and comment by ). 'Tri-site' and 'bi-site' modes of enzyme catalysis have been proposed . Tri-site catalysis requires that all three catalytic sites are occupied and interact with each other; in bi-site catalysis the enzyme functions with two substrate filled ca

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.ATPSYN-RXN|reaction.ecocyc.ATPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7041|reaction.ecocyc.RXN0-7041]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C03028|molecule.C03028]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (11)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.F-1-CPLX|complex.ecocyc.F-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.F-O-CPLX|complex.ecocyc.F-O-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A6E6|protein.P0A6E6]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AB98|protein.P0AB98]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABA0|protein.P0ABA0]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P0ABA4|protein.P0ABA4]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABA6|protein.P0ABA6]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABB0|protein.P0ABB0]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P0ABB4|protein.P0ABB4]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P68699|protein.P68699]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=10 | EcoCyc transporter component coefficient=10

## External IDs

- `EcoCyc:ATPSYN-CPLX`
- `PDB:1QO1`
- `PDB:1C17`
- `PDB:5T4Q`
- `PDB:5T4P`
- `PDB:5T4O`
- `PDB:6WNR`
- `PDB:6WNQ`
- `PDB:6VWK`
- `QSPROTEOME:QS00138407`

## Notes

1*complex.ecocyc.F-O-CPLX|1*complex.ecocyc.F-1-CPLX
