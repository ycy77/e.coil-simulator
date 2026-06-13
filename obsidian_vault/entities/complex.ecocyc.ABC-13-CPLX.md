---
entity_id: "complex.ecocyc.ABC-13-CPLX"
entity_type: "complex"
name: "glutamate / aspartate ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-13-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamate / aspartate ABC transporter

`complex.ecocyc.ABC-13-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-13-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P37902|protein.P37902]], [[protein.P0AER5|protein.P0AER5]], [[protein.P0AER3|protein.P0AER3]], [[protein.P0AAG3|protein.P0AAG3]]

## Enriched Summary

GltIJKL is an L-glutamate and L-aspartate uptake system that is a member of the ATP Binding Cassette (ABC) superfamily of transporters . GltI is the periplasmic-binding protein of the transporter complex ; GltJ and GltK are predicted integral membrane subunits and GltL is the predicted ATP binding subunit . E. coli contains a multiplicity of transport systems for the uptake of L-glutamate and L-aspartate; the contribution of various systems - including a binding protein dependent system (presumably GltIJKL) - as a percentage of total uptake has been assessed . GltIJKL is an L-glutamate and L-aspartate uptake system that is a member of the ATP Binding Cassette (ABC) superfamily of transporters . GltI is the periplasmic-binding protein of the transporter complex ; GltJ and GltK are predicted integral membrane subunits and GltL is the predicted ATP binding subunit . E. coli contains a multiplicity of transport systems for the uptake of L-glutamate and L-aspartate; the contribution of various systems - including a binding protein dependent system (presumably GltIJKL) - as a percentage of total uptake has been assessed .

## Biological Role

Catalyzes ABC-13-RXN (reaction.ecocyc.ABC-13-RXN), TRANS-RXN0-222 (reaction.ecocyc.TRANS-RXN0-222). Transports L-Glutamate (molecule.C00025), L-Aspartate (molecule.C00049), hν (molecule.ecocyc.Light).

## Annotation

GltIJKL is an L-glutamate and L-aspartate uptake system that is a member of the ATP Binding Cassette (ABC) superfamily of transporters . GltI is the periplasmic-binding protein of the transporter complex ; GltJ and GltK are predicted integral membrane subunits and GltL is the predicted ATP binding subunit . E. coli contains a multiplicity of transport systems for the uptake of L-glutamate and L-aspartate; the contribution of various systems - including a binding protein dependent system (presumably GltIJKL) - as a percentage of total uptake has been assessed .

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ABC-13-RXN|reaction.ecocyc.ABC-13-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-222|reaction.ecocyc.TRANS-RXN0-222]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AAG3|protein.P0AAG3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P0AER3|protein.P0AER3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AER5|protein.P0AER5]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P37902|protein.P37902]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-13-CPLX`
- `QSPROTEOME:QS00049301`

## Notes

1*protein.P37902|1*protein.P0AER5|1*protein.P0AER3|2*protein.P0AAG3
