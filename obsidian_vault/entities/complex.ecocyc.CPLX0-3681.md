---
entity_id: "complex.ecocyc.CPLX0-3681"
entity_type: "complex"
name: "ADP-L-glycero-D-mannoheptose 6-epimerase"
source_database: "EcoCyc"
source_id: "CPLX0-3681"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ADP-L-glycero-D-mannoheptose 6-epimerase

`complex.ecocyc.CPLX0-3681`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3681`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P67910|protein.P67910]]

## Enriched Summary

EcoCyc complex CPLX0-3681

## Biological Role

Catalyzes 5.1.3.20-RXN (reaction.ecocyc.5.1.3.20-RXN). Bound by NADP+ (molecule.C00006).

## Annotation

EcoCyc complex CPLX0-3681

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.5.1.3.20-RXN|reaction.ecocyc.5.1.3.20-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P67910|protein.P67910]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=5

## External IDs

- `EcoCyc:CPLX0-3681`
- `QSPROTEOME:QS00196515`

## Notes

5*protein.P67910
