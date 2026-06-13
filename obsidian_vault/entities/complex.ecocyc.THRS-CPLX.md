---
entity_id: "complex.ecocyc.THRS-CPLX"
entity_type: "complex"
name: "threonine—tRNA ligase"
source_database: "EcoCyc"
source_id: "THRS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "serine&mdash"
  - "tRNA<sup>Thr</sup> ligase"
---

# threonine—tRNA ligase

`complex.ecocyc.THRS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:THRS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8M3|protein.P0A8M3]]

## Enriched Summary

EcoCyc complex THRS-CPLX

## Biological Role

Catalyzes RXN-23947 (reaction.ecocyc.RXN-23947), RXN-23948 (reaction.ecocyc.RXN-23948), THREONINE--TRNA-LIGASE-RXN (reaction.ecocyc.THREONINE--TRNA-LIGASE-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex THRS-CPLX

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.RXN-23947|reaction.ecocyc.RXN-23947]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23948|reaction.ecocyc.RXN-23948]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THREONINE--TRNA-LIGASE-RXN|reaction.ecocyc.THREONINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `represses` --> [[gene.b1719|gene.b1719]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A8M3|protein.P0A8M3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:THRS-CPLX`
- `QSPROTEOME:QS00049555`

## Notes

2*protein.P0A8M3
