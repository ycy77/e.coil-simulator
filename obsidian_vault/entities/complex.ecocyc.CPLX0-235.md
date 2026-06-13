---
entity_id: "complex.ecocyc.CPLX0-235"
entity_type: "complex"
name: "glyoxylate reductase [multifunctional]"
source_database: "EcoCyc"
source_id: "CPLX0-235"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glyoxylate reductase [multifunctional]

`complex.ecocyc.CPLX0-235`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-235`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37666|protein.P37666]]

## Enriched Summary

GhrB is a 2-ketoaldonate reductase (2KR) using NADPH as the preferred electron donor . The enzyme has broad substrate specificity, utilizing both aromatic and aliphatic α-keto carboxylic acids . The reduction is stereospecific, producing the (R)-enantiomer . A ghrB null mutant can not utilize 2-keto-D-gluconate as the sole source of carbon . ghrB appears to be expressed constitutively . Inactivation of ghrB improves production of 1,2,4-butanetriol in a metabolically engineered strain . GhrB is a 2-ketoaldonate reductase (2KR) using NADPH as the preferred electron donor . The enzyme has broad substrate specificity, utilizing both aromatic and aliphatic α-keto carboxylic acids . The reduction is stereospecific, producing the (R)-enantiomer . A ghrB null mutant can not utilize 2-keto-D-gluconate as the sole source of carbon . ghrB appears to be expressed constitutively . Inactivation of ghrB improves production of 1,2,4-butanetriol in a metabolically engineered strain .

## Biological Role

Catalyzes 1.1.1.215-RXN (reaction.ecocyc.1.1.1.215-RXN), GLYOXYLATE-REDUCTASE-NADP+-RXN (reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN), hydroxypyruvate reductase (NADP+) (reaction.ecocyc.RXN0-300), L-idonate 2-dehydrogenase (reaction.ecocyc.RXN0-7021), 5-dehydro-D-gluconate 2-dehydrogenase (reaction.ecocyc.YIAE1-RXN).

## Annotation

GhrB is a 2-ketoaldonate reductase (2KR) using NADPH as the preferred electron donor . The enzyme has broad substrate specificity, utilizing both aromatic and aliphatic α-keto carboxylic acids . The reduction is stereospecific, producing the (R)-enantiomer . A ghrB null mutant can not utilize 2-keto-D-gluconate as the sole source of carbon . ghrB appears to be expressed constitutively . Inactivation of ghrB improves production of 1,2,4-butanetriol in a metabolically engineered strain .

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.1.1.1.215-RXN|reaction.ecocyc.1.1.1.215-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN|reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-300|reaction.ecocyc.RXN0-300]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7021|reaction.ecocyc.RXN0-7021]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.YIAE1-RXN|reaction.ecocyc.YIAE1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P37666|protein.P37666]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-235`
- `QSPROTEOME:QS00049584`

## Notes

2*protein.P37666
