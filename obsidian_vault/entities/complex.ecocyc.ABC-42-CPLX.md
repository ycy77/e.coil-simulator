---
entity_id: "complex.ecocyc.ABC-42-CPLX"
entity_type: "complex"
name: "D-allose ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-42-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# D-allose ABC transporter

`complex.ecocyc.ABC-42-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-42-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P32721|protein.P32721]], [[protein.P32720|protein.P32720]], [[protein.P39265|protein.P39265]]

## Enriched Summary

AlsBAC is a D-allose transporter that belongs to the ATP-binding Cassette (ABC) Superfamily. AlsBAC catalyses the uptake of D-allose, a rare hexose that can be used by E. coli K-12 MG1655 as a sole carbon source; AlsBAC can also transport ribose and may represent the system responsible for the reduced growth on ribose that is observed in the absence of the primary ribose transport system (RbsDAC) . Sequence similarity predicts that alsA encodes an ATP binding subunit and alsC encodes an integral membrane protein; AlsB is a periplasmic protein that binds D-allose with a Kd of 0.33μM . alsBAC is part of a larger operon (alsRBACE); expression of this operon is induced by D-allose (and by D-ribose when assayed in a ribose auxotroph) in an AlsR dependent manner . The complex stoichiometry represented here has not been experimentally demonstrated. AlsBAC is a D-allose transporter that belongs to the ATP-binding Cassette (ABC) Superfamily. AlsBAC catalyses the uptake of D-allose, a rare hexose that can be used by E. coli K-12 MG1655 as a sole carbon source; AlsBAC can also transport ribose and may represent the system responsible for the reduced growth on ribose that is observed in the absence of the primary ribose transport system (RbsDAC)...

## Biological Role

Catalyzes ABC-42-RXN (reaction.ecocyc.ABC-42-RXN). Transports D-Allose (molecule.C01487), hν (molecule.ecocyc.Light).

## Annotation

AlsBAC is a D-allose transporter that belongs to the ATP-binding Cassette (ABC) Superfamily. AlsBAC catalyses the uptake of D-allose, a rare hexose that can be used by E. coli K-12 MG1655 as a sole carbon source; AlsBAC can also transport ribose and may represent the system responsible for the reduced growth on ribose that is observed in the absence of the primary ribose transport system (RbsDAC) . Sequence similarity predicts that alsA encodes an ATP binding subunit and alsC encodes an integral membrane protein; AlsB is a periplasmic protein that binds D-allose with a Kd of 0.33μM . alsBAC is part of a larger operon (alsRBACE); expression of this operon is induced by D-allose (and by D-ribose when assayed in a ribose auxotroph) in an AlsR dependent manner . The complex stoichiometry represented here has not been experimentally demonstrated.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-42-RXN|reaction.ecocyc.ABC-42-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C01487|molecule.C01487]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P32720|protein.P32720]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P32721|protein.P32721]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P39265|protein.P39265]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-42-CPLX`
- `QSPROTEOME:QS00049323`

## Notes

1*protein.P32721|2*protein.P32720|1*protein.P39265
