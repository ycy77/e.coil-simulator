---
entity_id: "complex.ecocyc.CPLX0-7962"
entity_type: "complex"
name: "L-amino acid N-acyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-7962"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-amino acid N-acyltransferase

`complex.ecocyc.CPLX0-7962`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7962`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76112|protein.P76112]]

## Enriched Summary

In a patent application, the YncA protein is reported to have L-amino acid N-acyltransferase activity . In Salmonella enterica, overexpressed YncA is able to acetylate methionine sulfoximine (MSX) and methionine sulfone (MSO), but not phosphinothricin . MnaT: methionine N-acyltransferase In a patent application, the YncA protein is reported to have L-amino acid N-acyltransferase activity . In Salmonella enterica, overexpressed YncA is able to acetylate methionine sulfoximine (MSX) and methionine sulfone (MSO), but not phosphinothricin . MnaT: methionine N-acyltransferase

## Biological Role

Catalyzes RXN0-6948 (reaction.ecocyc.RXN0-6948).

## Annotation

In a patent application, the YncA protein is reported to have L-amino acid N-acyltransferase activity . In Salmonella enterica, overexpressed YncA is able to acetylate methionine sulfoximine (MSX) and methionine sulfone (MSO), but not phosphinothricin . MnaT: methionine N-acyltransferase

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6948|reaction.ecocyc.RXN0-6948]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76112|protein.P76112]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7962`
- `QSPROTEOME:QS00181707`

## Notes

2*protein.P76112
