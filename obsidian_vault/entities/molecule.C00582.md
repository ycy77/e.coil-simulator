---
entity_id: "molecule.C00582"
entity_type: "small_molecule"
name: "Phenylacetyl-CoA"
source_database: "KEGG"
source_id: "C00582"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phenylacetyl-CoA"
  - "Phenylacetyl coenzyme A"
---

# Phenylacetyl-CoA

`molecule.C00582`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00582`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phenylacetyl-CoA; Phenylacetyl coenzyme A

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Annotation

KEGG compound: Phenylacetyl-CoA; Phenylacetyl coenzyme A

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7729|complex.ecocyc.CPLX0-7729]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN-10819|reaction.ecocyc.RXN-10819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2042|reaction.ecocyc.RXN0-2042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5450|reaction.ecocyc.RXN0-5450]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7104|reaction.ecocyc.RXN0-7104]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00582`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
