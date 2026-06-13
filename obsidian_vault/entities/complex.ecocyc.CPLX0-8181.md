---
entity_id: "complex.ecocyc.CPLX0-8181"
entity_type: "complex"
name: "N6-L-threonylcarbamoyladenine synthase, TsaB-TsaD dimer subunit"
source_database: "EcoCyc"
source_id: "CPLX0-8181"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# N6-L-threonylcarbamoyladenine synthase, TsaB-TsaD dimer subunit

`complex.ecocyc.CPLX0-8181`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8181`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76256|protein.P76256]], [[protein.P05852|protein.P05852]]

## Enriched Summary

TsaB and TsaD form a heterodimer; crystal structures of this protein complex have been solved. The structure shows ADP bound at the dimer interface . TsaB and TsaD form a heterodimer; crystal structures of this protein complex have been solved. The structure shows ADP bound at the dimer interface .

## Biological Role

Component of N6-L-threonylcarbamoyladenine synthase (complex.ecocyc.CPLX0-8182).

## Annotation

TsaB and TsaD form a heterodimer; crystal structures of this protein complex have been solved. The structure shows ADP bound at the dimer interface .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8182|complex.ecocyc.CPLX0-8182]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P05852|protein.P05852]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P76256|protein.P76256]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8181`
- `PDB:4YDU`
- `PDB:4WQ4`
- `PDB:4WQ5`
- `PDB:6Z81`
- `QSPROTEOME:QS00196185`

## Notes

1*protein.P76256|1*protein.P05852
