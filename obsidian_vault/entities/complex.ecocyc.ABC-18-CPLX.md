---
entity_id: "complex.ecocyc.ABC-18-CPLX"
entity_type: "complex"
name: "D-galactose / methyl-β-D-galactoside ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-18-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MglBAC"
  - "MglP"
---

# D-galactose / methyl-β-D-galactoside ABC transporter

`complex.ecocyc.ABC-18-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-18-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P0AAG8|protein.P0AAG8]], [[protein.P23200|protein.P23200]], [[protein.P0AEE5|protein.P0AEE5]]

## Enriched Summary

MglBAC is a high affinity D-galactose/methyl-D-galactoside uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. MglB is a periplasmic galactose/methyl-galactoside binding protein (and galactose/glucose chemoreceptor); MglC is the predicted integral membrane component and MglA is the predicted ATP-binding component of the transporter complex The Mgl system and in particular the Mgl periplasmic binding protein were the focus of early investigation in E. coli K-12; the Mgl system transports galactose at µM concentrations (see for example . The Mgl system is differentiated from other D-galactose transport systems by its ability to transport methyl-β-galactosides; glucose is a substrate for the Mgl system but it is not an inducer; D-fucose induces the Mgl system and is a substrate but it is not metabolized further in E. coli K-12 (see and references within). MglBAC is a high affinity D-galactose/methyl-D-galactoside uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters...

## Biological Role

Catalyzes ABC-18-RXN (reaction.ecocyc.ABC-18-RXN), TRANS-RXN0-541 (reaction.ecocyc.TRANS-RXN0-541). Transports D-Galactose (molecule.C00124), Methyl beta-D-galactoside (molecule.C03619), hν (molecule.ecocyc.Light).

## Annotation

MglBAC is a high affinity D-galactose/methyl-D-galactoside uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. MglB is a periplasmic galactose/methyl-galactoside binding protein (and galactose/glucose chemoreceptor); MglC is the predicted integral membrane component and MglA is the predicted ATP-binding component of the transporter complex The Mgl system and in particular the Mgl periplasmic binding protein were the focus of early investigation in E. coli K-12; the Mgl system transports galactose at µM concentrations (see for example . The Mgl system is differentiated from other D-galactose transport systems by its ability to transport methyl-β-galactosides; glucose is a substrate for the Mgl system but it is not an inducer; D-fucose induces the Mgl system and is a substrate but it is not metabolized further in E. coli K-12 (see and references within).

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ABC-18-RXN|reaction.ecocyc.ABC-18-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-541|reaction.ecocyc.TRANS-RXN0-541]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C03619|molecule.C03619]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AAG8|protein.P0AAG8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AEE5|protein.P0AEE5]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P23200|protein.P23200]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-18-CPLX`
- `QSPROTEOME:QS00049304`

## Notes

1*protein.P0AAG8|2*protein.P23200|1*protein.P0AEE5
