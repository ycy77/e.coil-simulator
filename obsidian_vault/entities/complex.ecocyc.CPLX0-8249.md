---
entity_id: "complex.ecocyc.CPLX0-8249"
entity_type: "complex"
name: "5-oxoprolinase"
source_database: "EcoCyc"
source_id: "CPLX0-8249"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 5-oxoprolinase

`complex.ecocyc.CPLX0-8249`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8249`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P75745|protein.P75745]], [[protein.P0AAV4|protein.P0AAV4]], [[protein.P75746|protein.P75746]]

## Enriched Summary

Prokaryotic 5-oxo-L-prolinase activity was discovered in Bacillus subtilis using genome context methods . Overexpression of pxpBCA together leads to the presence of detectable oxoprolinase activity in cell lysates. A pxpC deletion mutant grows to a lower OD than wild type in minimal medium with ammonium as the sole source of nitrogen . Note that the existence of a PxpABC protein complex has not been shown. In B. subtilis, the PxpB and PxpC proteins interact, and all three proteins are required for 5-oxoprolinase activity. Prokaryotic 5-oxo-L-prolinase activity was discovered in Bacillus subtilis using genome context methods . Overexpression of pxpBCA together leads to the presence of detectable oxoprolinase activity in cell lysates. A pxpC deletion mutant grows to a lower OD than wild type in minimal medium with ammonium as the sole source of nitrogen . Note that the existence of a PxpABC protein complex has not been shown. In B. subtilis, the PxpB and PxpC proteins interact, and all three proteins are required for 5-oxoprolinase activity.

## Biological Role

Catalyzes 5-OXOPROLINASE-ATP-HYDROLYSING-RXN (reaction.ecocyc.5-OXOPROLINASE-ATP-HYDROLYSING-RXN).

## Annotation

Prokaryotic 5-oxo-L-prolinase activity was discovered in Bacillus subtilis using genome context methods . Overexpression of pxpBCA together leads to the presence of detectable oxoprolinase activity in cell lysates. A pxpC deletion mutant grows to a lower OD than wild type in minimal medium with ammonium as the sole source of nitrogen . Note that the existence of a PxpABC protein complex has not been shown. In B. subtilis, the PxpB and PxpC proteins interact, and all three proteins are required for 5-oxoprolinase activity.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.5-OXOPROLINASE-ATP-HYDROLYSING-RXN|reaction.ecocyc.5-OXOPROLINASE-ATP-HYDROLYSING-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AAV4|protein.P0AAV4]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P75745|protein.P75745]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P75746|protein.P75746]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8249`
- `PDB:5DUD`
- `QSPROTEOME:QS00049466`

## Notes

protein.P75745|protein.P0AAV4|protein.P75746
