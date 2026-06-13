---
entity_id: "complex.ecocyc.PYRROLINECARBREDUCT-CPLX"
entity_type: "complex"
name: "pyrroline-5-carboxylate reductase"
source_database: "EcoCyc"
source_id: "PYRROLINECARBREDUCT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pyrroline-5-carboxylate reductase

`complex.ecocyc.PYRROLINECARBREDUCT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PYRROLINECARBREDUCT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9L8|protein.P0A9L8]]

## Enriched Summary

The final step in the PROSYN-PWY pathway, the reduction of L-DELTA1-PYRROLINE_5-CARBOXYLATE (PCA) to PRO, is catalyzed by NADPH-dependent pyrroline-5-carboxylate reductase (PCA reductase) . While synthesis of ProC is not repressed by proline, the enzyme activity is inhibited by the reaction end products, proline and NADP . Review: The final step in the PROSYN-PWY pathway, the reduction of L-DELTA1-PYRROLINE_5-CARBOXYLATE (PCA) to PRO, is catalyzed by NADPH-dependent pyrroline-5-carboxylate reductase (PCA reductase) . While synthesis of ProC is not repressed by proline, the enzyme activity is inhibited by the reaction end products, proline and NADP . Review:

## Biological Role

Catalyzes PYRROLINECARBREDUCT-RXN (reaction.ecocyc.PYRROLINECARBREDUCT-RXN).

## Annotation

The final step in the PROSYN-PWY pathway, the reduction of L-DELTA1-PYRROLINE_5-CARBOXYLATE (PCA) to PRO, is catalyzed by NADPH-dependent pyrroline-5-carboxylate reductase (PCA reductase) . While synthesis of ProC is not repressed by proline, the enzyme activity is inhibited by the reaction end products, proline and NADP . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PYRROLINECARBREDUCT-RXN|reaction.ecocyc.PYRROLINECARBREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9L8|protein.P0A9L8]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:PYRROLINECARBREDUCT-CPLX`
- `QSPROTEOME:QS00196205`

## Notes

10*protein.P0A9L8
