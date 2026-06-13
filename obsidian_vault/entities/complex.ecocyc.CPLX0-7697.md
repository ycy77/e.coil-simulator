---
entity_id: "complex.ecocyc.CPLX0-7697"
entity_type: "complex"
name: "MukEF complex"
source_database: "EcoCyc"
source_id: "CPLX0-7697"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# MukEF complex

`complex.ecocyc.CPLX0-7697`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7697`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P22524|protein.P22524]], [[complex.ecocyc.CPLX0-7698|complex.ecocyc.CPLX0-7698]]

## Enriched Summary

The MukEF complex forms an elongated shape that is either asymmetric or dimeric . In vivo experiments suggest the presence of nearly equimolar amounts of F2E2 and F2E4 . A crystal structure of the MukEF complex allowed identification of interacting surfaces in MukE that are important for assembling a functional MukBEF complex . The MukEF complex forms an elongated shape that is either asymmetric or dimeric . In vivo experiments suggest the presence of nearly equimolar amounts of F2E2 and F2E4 . A crystal structure of the MukEF complex allowed identification of interacting surfaces in MukE that are important for assembling a functional MukBEF complex .

## Biological Role

Component of bacterial condensin MukBEF (complex.ecocyc.CPLX0-2561).

## Annotation

The MukEF complex forms an elongated shape that is either asymmetric or dimeric . In vivo experiments suggest the presence of nearly equimolar amounts of F2E2 and F2E4 . A crystal structure of the MukEF complex allowed identification of interacting surfaces in MukE that are important for assembling a functional MukBEF complex .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2561|complex.ecocyc.CPLX0-2561]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (3)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7698|complex.ecocyc.CPLX0-7698]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P22524|protein.P22524]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P60293|protein.P60293]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7697`
- `PDB:3EUH`
- `PDB:3RPU`
- `QSPROTEOME:QS00049436`

## Notes

4*protein.P22524|1*complex.ecocyc.CPLX0-7698
