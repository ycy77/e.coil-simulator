---
entity_id: "complex.ecocyc.CPLX0-230"
entity_type: "complex"
name: "isocitrate dehydrogenase kinase / isocitrate dehydrogenase phosphatase"
source_database: "EcoCyc"
source_id: "CPLX0-230"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# isocitrate dehydrogenase kinase / isocitrate dehydrogenase phosphatase

`complex.ecocyc.CPLX0-230`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-230`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P11071|protein.P11071]]

## Enriched Summary

EcoCyc complex CPLX0-230

## Biological Role

Catalyzes dephosphorylation of isocitrate dehydrogenase enzyme (reaction.ecocyc.DEPHOSICITDEHASE-RXN), PHOSICITDEHASE-RXN (reaction.ecocyc.PHOSICITDEHASE-RXN). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex CPLX0-230

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.DEPHOSICITDEHASE-RXN|reaction.ecocyc.DEPHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PHOSICITDEHASE-RXN|reaction.ecocyc.PHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P11071|protein.P11071]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-230`
- `QSPROTEOME:QS00191917`

## Notes

2*protein.P11071
