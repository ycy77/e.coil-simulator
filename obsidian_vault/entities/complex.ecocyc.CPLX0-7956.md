---
entity_id: "complex.ecocyc.CPLX0-7956"
entity_type: "complex"
name: "carbon storage regulator CsrA"
source_database: "EcoCyc"
source_id: "CPLX0-7956"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# carbon storage regulator CsrA

`complex.ecocyc.CPLX0-7956`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7956`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69913|protein.P69913]]

## Enriched Summary

EcoCyc complex CPLX0-7956

## Biological Role

Component of CsrA complex with McaS RNA (complex.ecocyc.CPLX0-8028).

## Annotation

EcoCyc complex CPLX0-7956

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8028|complex.ecocyc.CPLX0-8028]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0020|gene.b0020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b1276|gene.b1276]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b1916|gene.b1916]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b2369|gene.b2369]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P69913|protein.P69913]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7956`
- `QSPROTEOME:QS00196529`

## Notes

2*protein.P69913
