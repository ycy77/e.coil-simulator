---
entity_id: "complex.ecocyc.NQOR-CPLX"
entity_type: "complex"
name: "NADH dehydrogenase (quinone)"
source_database: "EcoCyc"
source_id: "NQOR-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NADH dehydrogenase (quinone)

`complex.ecocyc.NQOR-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NQOR-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.ecocyc.NQOR-MONOMER|protein.ecocyc.NQOR-MONOMER]]

## Enriched Summary

This NADH dehydrogenase enzyme is thought to compete with the one-electron reduction pathway of quinones, which is potentially toxic as it generates superoxide radicals and hydrogen peroxide . The intracellular level of this enzyme is increased 23-fold by growth in the presence of 0.3 mM menadione, but not paraquat . The critical inductive signal is a 2-alkyl-1.4-quinone structure with an unsubstitued or Br-substituted C-3 . No gene has been identified for this enzyme yet. Based on its properties, it is possible that this enzyme is identical to either CPLX0-7632 or CPLX0-3121. This NADH dehydrogenase enzyme is thought to compete with the one-electron reduction pathway of quinones, which is potentially toxic as it generates superoxide radicals and hydrogen peroxide . The intracellular level of this enzyme is increased 23-fold by growth in the presence of 0.3 mM menadione, but not paraquat . The critical inductive signal is a 2-alkyl-1.4-quinone structure with an unsubstitued or Br-substituted C-3 . No gene has been identified for this enzyme yet. Based on its properties, it is possible that this enzyme is identical to either CPLX0-7632 or CPLX0-3121.

## Biological Role

Catalyzes NADH dehydrogenase (quinone) (reaction.ecocyc.NADH-DEHYDROGENASE-QUINONE-RXN). Bound by FMN (molecule.C00061).

## Annotation

This NADH dehydrogenase enzyme is thought to compete with the one-electron reduction pathway of quinones, which is potentially toxic as it generates superoxide radicals and hydrogen peroxide . The intracellular level of this enzyme is increased 23-fold by growth in the presence of 0.3 mM menadione, but not paraquat . The critical inductive signal is a 2-alkyl-1.4-quinone structure with an unsubstitued or Br-substituted C-3 . No gene has been identified for this enzyme yet. Based on its properties, it is possible that this enzyme is identical to either CPLX0-7632 or CPLX0-3121.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NADH-DEHYDROGENASE-QUINONE-RXN|reaction.ecocyc.NADH-DEHYDROGENASE-QUINONE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.ecocyc.NQOR-MONOMER|protein.ecocyc.NQOR-MONOMER]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:NQOR-CPLX`

## Notes

2*protein.ecocyc.NQOR-MONOMER
