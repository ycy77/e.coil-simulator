---
entity_id: "complex.ecocyc.CPLX0-7979"
entity_type: "complex"
name: "monoacetylchitobiose-6-phosphate hydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-7979"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# monoacetylchitobiose-6-phosphate hydrolase

`complex.ecocyc.CPLX0-7979`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7979`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P17411|protein.P17411]]

## Enriched Summary

EcoCyc complex CPLX0-7979

## Biological Role

Catalyzes 6-PHOSPHO-BETA-GLUCOSIDASE-RXN (reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN), RXN0-7392 (reaction.ecocyc.RXN0-7392). Bound by NAD+ (molecule.C00003), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex CPLX0-7979

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN|reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7392|reaction.ecocyc.RXN0-7392]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P17411|protein.P17411]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7979`
- `QSPROTEOME:QS00049685`

## Notes

4*protein.P17411
