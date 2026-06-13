---
entity_id: "complex.ecocyc.DIHYDROPTERIREDUCT-CPLX"
entity_type: "complex"
name: "NAD(P)H-dependent nitroreductase NfsB"
source_database: "EcoCyc"
source_id: "DIHYDROPTERIREDUCT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NAD(P)H-dependent nitroreductase NfsB

`complex.ecocyc.DIHYDROPTERIREDUCT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DIHYDROPTERIREDUCT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P38489|protein.P38489]]

## Enriched Summary

EcoCyc complex DIHYDROPTERIREDUCT-CPLX

## Biological Role

Catalyzes 1.5.1.34-RXN (reaction.ecocyc.1.5.1.34-RXN), RXN-13853 (reaction.ecocyc.RXN-13853), RXN0-7386 (reaction.ecocyc.RXN0-7386). Bound by FAD (molecule.C00016), FMN (molecule.C00061).

## Annotation

EcoCyc complex DIHYDROPTERIREDUCT-CPLX

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.1.5.1.34-RXN|reaction.ecocyc.1.5.1.34-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-13853|reaction.ecocyc.RXN-13853]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7386|reaction.ecocyc.RXN0-7386]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P38489|protein.P38489]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DIHYDROPTERIREDUCT-CPLX`
- `QSPROTEOME:QS00190535`

## Notes

2*protein.P38489
