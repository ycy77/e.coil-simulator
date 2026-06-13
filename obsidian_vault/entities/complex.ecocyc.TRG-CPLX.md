---
entity_id: "complex.ecocyc.TRG-CPLX"
entity_type: "complex"
name: "chemotaxis signaling complex core unit - ribose/galactose/glucose sensing"
source_database: "EcoCyc"
source_id: "TRG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MCP-III signaling complex"
---

# chemotaxis signaling complex core unit - ribose/galactose/glucose sensing

`complex.ecocyc.TRG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TRG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CHEA-CPLX|complex.ecocyc.CHEA-CPLX]], [[protein.P0A964|protein.P0A964]], [[complex.ecocyc.CPLX0-8105|complex.ecocyc.CPLX0-8105]]

## Enriched Summary

EcoCyc complex TRG-CPLX

## Annotation

EcoCyc complex TRG-CPLX

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CHEA-CPLX|complex.ecocyc.CHEA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CPLX0-8105|complex.ecocyc.CPLX0-8105]] `EcoCyc` `database` - EcoCyc component coefficient=6
- `is_component_of` <-- [[protein.P05704|protein.P05704]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TRG-CPLX`
- `PDB:6S1K`

## Notes

1*complex.ecocyc.CHEA-CPLX|2*protein.P0A964|6*complex.ecocyc.CPLX0-8105
