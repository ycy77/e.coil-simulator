---
entity_id: "complex.ecocyc.CPLX0-7794"
entity_type: "complex"
name: "3-sulfolactaldehyde reductase"
source_database: "EcoCyc"
source_id: "CPLX0-7794"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-sulfolactaldehyde reductase

`complex.ecocyc.CPLX0-7794`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7794`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9V8|protein.P0A9V8]]

## Enriched Summary

3-Sulfolactaldehyde reductase (YihU) catalyzes the NADH-dependent reduction of CPD-16503 to 2-3-dihydroxypropane-1-sulfonate, which is excreted from the cell . Screening for enzymatic activity by metabolite profiling suggested that YihU has γ-hydroxybutyrate dehydrogenase activity. In vitro, the enzyme preferentially catalyzes the reaction in the succinate semialdehyde (SSA) reductase direction. YihU may play a role in detoxification of SSA . Expression of YihU is induced by growth on CPD-10247 . A yihU deletion mutant is more sensitive to toxic levels of SSA than wild type . 3-Sulfolactaldehyde reductase (YihU) catalyzes the NADH-dependent reduction of CPD-16503 to 2-3-dihydroxypropane-1-sulfonate, which is excreted from the cell . Screening for enzymatic activity by metabolite profiling suggested that YihU has γ-hydroxybutyrate dehydrogenase activity. In vitro, the enzyme preferentially catalyzes the reaction in the succinate semialdehyde (SSA) reductase direction. YihU may play a role in detoxification of SSA . Expression of YihU is induced by growth on CPD-10247 . A yihU deletion mutant is more sensitive to toxic levels of SSA than wild type .

## Biological Role

Catalyzes 4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN (reaction.ecocyc.4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN), RXN-15299 (reaction.ecocyc.RXN-15299).

## Annotation

3-Sulfolactaldehyde reductase (YihU) catalyzes the NADH-dependent reduction of CPD-16503 to 2-3-dihydroxypropane-1-sulfonate, which is excreted from the cell . Screening for enzymatic activity by metabolite profiling suggested that YihU has γ-hydroxybutyrate dehydrogenase activity. In vitro, the enzyme preferentially catalyzes the reaction in the succinate semialdehyde (SSA) reductase direction. YihU may play a role in detoxification of SSA . Expression of YihU is induced by growth on CPD-10247 . A yihU deletion mutant is more sensitive to toxic levels of SSA than wild type .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN|reaction.ecocyc.4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15299|reaction.ecocyc.RXN-15299]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9V8|protein.P0A9V8]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7794`
- `QSPROTEOME:QS00182001`

## Notes

4*protein.P0A9V8
