---
entity_id: "complex.ecocyc.CPLX0-8015"
entity_type: "complex"
name: "ethanol dehydrogenase / alcohol dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-8015"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ethanol dehydrogenase / alcohol dehydrogenase

`complex.ecocyc.CPLX0-8015`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8015`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39451|protein.P39451]]

## Enriched Summary

AdhP is an ethanol-active medium-chain alcohol dehydrogenase/acetaldehyde reductase. The enzyme is more efficient in the reverse direction of acetaldehyde reduction . AdhP activity contributes to the conversion of isobutyraldehyde to isobutanol in an engineered strain . AdhP did not show dehydrogenase activity in a high-throughput screen of purified proteins . Crystal structures of AdhP has been solved . Expression of AdhP is inducible by ethanol . AdhP is an ethanol-active medium-chain alcohol dehydrogenase/acetaldehyde reductase. The enzyme is more efficient in the reverse direction of acetaldehyde reduction . AdhP activity contributes to the conversion of isobutyraldehyde to isobutanol in an engineered strain . AdhP did not show dehydrogenase activity in a high-throughput screen of purified proteins . Crystal structures of AdhP has been solved . Expression of AdhP is inducible by ethanol .

## Biological Role

Catalyzes ALCOHOL-DEHYDROG-GENERIC-RXN (reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN), ALCOHOL-DEHYDROG-RXN (reaction.ecocyc.ALCOHOL-DEHYDROG-RXN).

## Annotation

AdhP is an ethanol-active medium-chain alcohol dehydrogenase/acetaldehyde reductase. The enzyme is more efficient in the reverse direction of acetaldehyde reduction . AdhP activity contributes to the conversion of isobutyraldehyde to isobutanol in an engineered strain . AdhP did not show dehydrogenase activity in a high-throughput screen of purified proteins . Crystal structures of AdhP has been solved . Expression of AdhP is inducible by ethanol .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P39451|protein.P39451]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8015`
- `QSPROTEOME:QS00183199`

## Notes

4*protein.P39451
