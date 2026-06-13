---
entity_id: "complex.ecocyc.CPLX0-8566"
entity_type: "complex"
name: "NtrC phosphorylated dimer"
source_database: "EcoCyc"
source_id: "CPLX0-8566"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NtrC phosphorylated dimer

`complex.ecocyc.CPLX0-8566`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8566`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P0AFB8|protein.P0AFB8]]

## Enriched Summary

EcoCyc complex CPLX0-8566

## Biological Role

Component of DNA-binding transcriptional dual regulator NtrC-phosphorylated (complex.ecocyc.PROTEIN-NRIP).

## Annotation

EcoCyc complex CPLX0-8566

## Outgoing Edges (5)

- `activates` --> [[gene.b1987|gene.b1987]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1988|gene.b1988]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2309|gene.b2309]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `is_component_of` --> [[complex.ecocyc.PROTEIN-NRIP|complex.ecocyc.PROTEIN-NRIP]] `EcoCyc` `database` - EcoCyc component coefficient=3
- `represses` --> [[gene.b1781|gene.b1781]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AFB8|protein.P0AFB8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8566`

## Notes

2*protein.P0AFB8
