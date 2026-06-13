---
entity_id: "complex.ecocyc.OROTPDECARB-CPLX"
entity_type: "complex"
name: "orotidine-5'-phosphate decarboxylase"
source_database: "EcoCyc"
source_id: "OROTPDECARB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# orotidine-5'-phosphate decarboxylase

`complex.ecocyc.OROTPDECARB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:OROTPDECARB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08244|protein.P08244]]

## Enriched Summary

Orotidine-5'-phosphate-decarboxylase (PyrF) catalyzes the last essential step in the de novo biosynthesis of pyrimidines, the synthesis of UMP by decarboxylation of orotidine-5'-phosphate. The enzyme is extremely proficient; the non-enzymatic rate of OMP decarboxylation at room temperature is extremely low at 2.8 x 10-16 s-1 . PyrF enhances the reaction rate by a factor of 1017, and the catalytic mechanism underlying this high efficiency has been the subject of investigation and debate . PyrF is a dimer in solution . Crystal structures of the enzyme have been solved . Computational simulations of proposed reaction mechanisms have been performed . pyrF mutants excrete orotic acid under conditions when normal strains excrete uracil . Strains deficient in CPLX0-3521 show higher PyrF activity than wild-type strains . Reviews: Orotidine-5'-phosphate-decarboxylase (PyrF) catalyzes the last essential step in the de novo biosynthesis of pyrimidines, the synthesis of UMP by decarboxylation of orotidine-5'-phosphate. The enzyme is extremely proficient; the non-enzymatic rate of OMP decarboxylation at room temperature is extremely low at 2.8 x 10-16 s-1 . PyrF enhances the reaction rate by a factor of 1017, and the catalytic mechanism underlying this high efficiency has been the subject of investigation and debate . PyrF is a dimer in solution...

## Biological Role

Catalyzes OROTPDECARB-RXN (reaction.ecocyc.OROTPDECARB-RXN).

## Annotation

Orotidine-5'-phosphate-decarboxylase (PyrF) catalyzes the last essential step in the de novo biosynthesis of pyrimidines, the synthesis of UMP by decarboxylation of orotidine-5'-phosphate. The enzyme is extremely proficient; the non-enzymatic rate of OMP decarboxylation at room temperature is extremely low at 2.8 x 10-16 s-1 . PyrF enhances the reaction rate by a factor of 1017, and the catalytic mechanism underlying this high efficiency has been the subject of investigation and debate . PyrF is a dimer in solution . Crystal structures of the enzyme have been solved . Computational simulations of proposed reaction mechanisms have been performed . pyrF mutants excrete orotic acid under conditions when normal strains excrete uracil . Strains deficient in CPLX0-3521 show higher PyrF activity than wild-type strains . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.OROTPDECARB-RXN|reaction.ecocyc.OROTPDECARB-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P08244|protein.P08244]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:OROTPDECARB-CPLX`
- `QSPROTEOME:QS00181737`

## Notes

2*protein.P08244
