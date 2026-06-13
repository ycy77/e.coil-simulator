---
entity_id: "molecule.C01099"
entity_type: "small_molecule"
name: "L-Fuculose 1-phosphate"
source_database: "KEGG"
source_id: "C01099"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Fuculose 1-phosphate"
---

# L-Fuculose 1-phosphate

`molecule.C01099`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01099`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Fuculose 1-phosphate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Annotation

KEGG compound: L-Fuculose 1-phosphate

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7650|complex.ecocyc.CPLX0-7650]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.FUCULOKIN-RXN|reaction.ecocyc.FUCULOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.FUCPALDOL-RXN|reaction.ecocyc.FUCPALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5307|reaction.ecocyc.RXN0-5307]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01099`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
