---
entity_id: "complex.ecocyc.CPLX0-7827"
entity_type: "complex"
name: "putative glutamate—cysteine ligase 2"
source_database: "EcoCyc"
source_id: "CPLX0-7827"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative glutamate—cysteine ligase 2

`complex.ecocyc.CPLX0-7827`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7827`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77213|protein.P77213]]

## Enriched Summary

Purified YbdK catalyzes the ATP-dependent ligation of glutamate with cysteine at a low catalytic rate. The enzyme binds ATP in a Mg2+-dependent manner . A crystal structure of YbdK was solved at 2.15 Å resolution, showing a fold similar to glutamine synthetase, but suggesting a different substrate specificity . Purified YbdK catalyzes the ATP-dependent ligation of glutamate with cysteine at a low catalytic rate. The enzyme binds ATP in a Mg2+-dependent manner . A crystal structure of YbdK was solved at 2.15 Å resolution, showing a fold similar to glutamine synthetase, but suggesting a different substrate specificity .

## Biological Role

Catalyzes GLUTCYSLIG-RXN (reaction.ecocyc.GLUTCYSLIG-RXN).

## Annotation

Purified YbdK catalyzes the ATP-dependent ligation of glutamate with cysteine at a low catalytic rate. The enzyme binds ATP in a Mg2+-dependent manner . A crystal structure of YbdK was solved at 2.15 Å resolution, showing a fold similar to glutamine synthetase, but suggesting a different substrate specificity .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTCYSLIG-RXN|reaction.ecocyc.GLUTCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77213|protein.P77213]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7827`
- `QSPROTEOME:QS00181755`

## Notes

2*protein.P77213
