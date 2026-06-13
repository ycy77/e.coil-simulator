---
entity_id: "complex.ecocyc.ADHE-CPLX"
entity_type: "complex"
name: "fused acetaldehyde-CoA dehydrogenase and Fe-dependent alcohol dehydrogenase"
source_database: "EcoCyc"
source_id: "ADHE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "fused acetaldehyde-CoA dehydrogenase and iron-dependent alcohol dehydrogenase"
---

# fused acetaldehyde-CoA dehydrogenase and Fe-dependent alcohol dehydrogenase

`complex.ecocyc.ADHE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ADHE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9Q7|protein.P0A9Q7]]

## Enriched Summary

EcoCyc complex ADHE-CPLX

## Biological Role

Catalyzes ACETALD-DEHYDROG-RXN (reaction.ecocyc.ACETALD-DEHYDROG-RXN), ALCOHOL-DEHYDROG-GENERIC-RXN (reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN), ALCOHOL-DEHYDROG-RXN (reaction.ecocyc.ALCOHOL-DEHYDROG-RXN), PFLDEACTIV-RXN (reaction.ecocyc.PFLDEACTIV-RXN). Bound by Fe2+ (molecule.C14818).

## Annotation

EcoCyc complex ADHE-CPLX

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PFLDEACTIV-RXN|reaction.ecocyc.PFLDEACTIV-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9Q7|protein.P0A9Q7]] `EcoCyc` `database` - EcoCyc component coefficient=40 | EcoCyc protcplxs.col coefficient=40

## External IDs

- `EcoCyc:ADHE-CPLX`

## Notes

40*protein.P0A9Q7
