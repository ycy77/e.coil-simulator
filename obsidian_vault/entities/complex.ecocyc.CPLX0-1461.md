---
entity_id: "complex.ecocyc.CPLX0-1461"
entity_type: "complex"
name: "Hfq"
source_database: "EcoCyc"
source_id: "CPLX0-1461"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Hfq"
  - "host factor for RNA phage Q &beta"
  - "replication"
---

# Hfq

`complex.ecocyc.CPLX0-1461`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1461`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P0A6X3|protein.P0A6X3]]

## Enriched Summary

EcoCyc complex CPLX0-1461

## Annotation

EcoCyc complex CPLX0-1461

## Outgoing Edges (2)

- `represses` --> [[gene.b1243|gene.b1243]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b2155|gene.b2155]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6X3|protein.P0A6X3]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-1461`
- `QSPROTEOME:QS00049595`

## Notes

6*protein.P0A6X3
