---
entity_id: "complex.ecocyc.ABC-64-CPLX"
entity_type: "complex"
name: "taurine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-64-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# taurine ABC transporter

`complex.ecocyc.ABC-64-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-64-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q47537|protein.Q47537]], [[protein.Q47539|protein.Q47539]], [[protein.Q47538|protein.Q47538]]

## Enriched Summary

TauA, TauB and TauC are the protein components of an ATP-dependent uptake system for taurine (2-aminoethanesulfonate) - an organosulfur compound which E. coli K-12 can use as a sulfur source under aerobic condtions. tauB and tauC insertion mutants are unable to grow with taurine as a sulfur source but can grow with a number of other sulfur sources (sulfate, lanthionine, methionine, glutathione, thioglycolate, cysteine, homocysteine, cystine, djenkolate plus others); growth on taurine is restored when tauABCD is expressed from a plasmid . tauABC is predicted to encode the components of an ABC transport system for taurine; TauB and TauC show strong sequence similarities to ATP-binding components and membrane components, respectively, of other members of the ABC superfamily; TauA contains a putative signal sequence and may be the periplasmic binding protein of the transport system . TauABC is able to transport a range of sulfonates including PIPES, 2-(4-pyridyl)ethanesulfonate, isethionate, 1,3-dioxo-2-isoindolineethanesulfonate, 3-aminopropanesulfonate, butanesulfonate and pentanesulfonate . E. coli K-12 contains a second ABC transporter (ABC-56-CPLX "SsuACB") for the uptake of alkanesulfonates; the two systems appear to complement each other with repect to the range of substrates transported...

## Biological Role

Catalyzes ABC-64-RXN (reaction.ecocyc.ABC-64-RXN). Transports Taurine (molecule.C00245), hν (molecule.ecocyc.Light).

## Annotation

TauA, TauB and TauC are the protein components of an ATP-dependent uptake system for taurine (2-aminoethanesulfonate) - an organosulfur compound which E. coli K-12 can use as a sulfur source under aerobic condtions. tauB and tauC insertion mutants are unable to grow with taurine as a sulfur source but can grow with a number of other sulfur sources (sulfate, lanthionine, methionine, glutathione, thioglycolate, cysteine, homocysteine, cystine, djenkolate plus others); growth on taurine is restored when tauABCD is expressed from a plasmid . tauABC is predicted to encode the components of an ABC transport system for taurine; TauB and TauC show strong sequence similarities to ATP-binding components and membrane components, respectively, of other members of the ABC superfamily; TauA contains a putative signal sequence and may be the periplasmic binding protein of the transport system . TauABC is able to transport a range of sulfonates including PIPES, 2-(4-pyridyl)ethanesulfonate, isethionate, 1,3-dioxo-2-isoindolineethanesulfonate, 3-aminopropanesulfonate, butanesulfonate and pentanesulfonate . E. coli K-12 contains a second ABC transporter (ABC-56-CPLX "SsuACB") for the uptake of alkanesulfonates; the two systems appear to complement each other with repect to the range of substrates transported . tauA, tauB and tauC form an operon with tauD (encoding taurine dioxygenase); expression is repressed in the presence of sulfate and induced by sulfate starvation . Reviews:

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-64-RXN|reaction.ecocyc.ABC-64-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00245|molecule.C00245]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.Q47537|protein.Q47537]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.Q47538|protein.Q47538]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.Q47539|protein.Q47539]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-64-CPLX`
- `QSPROTEOME:QS00197831`

## Notes

1*protein.Q47537|2*protein.Q47539|2*protein.Q47538
