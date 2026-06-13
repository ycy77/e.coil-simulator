---
entity_id: "complex.ecocyc.CPLX0-7951"
entity_type: "complex"
name: "2-hydroxypentadienoate hydratase"
source_database: "EcoCyc"
source_id: "CPLX0-7951"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-hydroxypentadienoate hydratase

`complex.ecocyc.CPLX0-7951`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7951`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77608|protein.P77608]]

## Enriched Summary

2-hydroxypentadienoate hydratase (MhpD) converts 2-hydroxypenta-2,4-dienoate (HPD) into 4-hydroxy-2-ketopentanoate . E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving MhpD is used for the catabolism of 3-(3-hydroxyphenyl)propionate . 2-hydroxypentadienoate hydratase (MhpD) converts 2-hydroxypenta-2,4-dienoate (HPD) into 4-hydroxy-2-ketopentanoate . E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving MhpD is used for the catabolism of 3-(3-hydroxyphenyl)propionate .

## Biological Role

Catalyzes 2-OXOPENT-4-ENOATE-HYDRATASE-RXN (reaction.ecocyc.2-OXOPENT-4-ENOATE-HYDRATASE-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

2-hydroxypentadienoate hydratase (MhpD) converts 2-hydroxypenta-2,4-dienoate (HPD) into 4-hydroxy-2-ketopentanoate . E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving MhpD is used for the catabolism of 3-(3-hydroxyphenyl)propionate .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2-OXOPENT-4-ENOATE-HYDRATASE-RXN|reaction.ecocyc.2-OXOPENT-4-ENOATE-HYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77608|protein.P77608]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=5

## External IDs

- `EcoCyc:CPLX0-7951`
- `QSPROTEOME:QS00049682`

## Notes

5*protein.P77608
