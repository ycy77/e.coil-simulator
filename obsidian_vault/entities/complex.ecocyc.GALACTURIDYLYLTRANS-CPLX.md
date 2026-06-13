---
entity_id: "complex.ecocyc.GALACTURIDYLYLTRANS-CPLX"
entity_type: "complex"
name: "galactose-1-phosphate uridylyltransferase"
source_database: "EcoCyc"
source_id: "GALACTURIDYLYLTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# galactose-1-phosphate uridylyltransferase

`complex.ecocyc.GALACTURIDYLYLTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GALACTURIDYLYLTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09148|protein.P09148]]

## Enriched Summary

EcoCyc complex GALACTURIDYLYLTRANS-CPLX

## Biological Role

Catalyzes GALACTURIDYLYLTRANS-RXN (reaction.ecocyc.GALACTURIDYLYLTRANS-RXN). Bound by Zinc cation (molecule.C00038), Fe2+ (molecule.C14818).

## Annotation

EcoCyc complex GALACTURIDYLYLTRANS-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GALACTURIDYLYLTRANS-RXN|reaction.ecocyc.GALACTURIDYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P09148|protein.P09148]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GALACTURIDYLYLTRANS-CPLX`
- `QSPROTEOME:QS00195305`

## Notes

2*protein.P09148
