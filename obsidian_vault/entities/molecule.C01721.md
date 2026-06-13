---
entity_id: "molecule.C01721"
entity_type: "small_molecule"
name: "L-Fuculose"
source_database: "KEGG"
source_id: "C01721"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Fuculose"
  - "6-Deoxy-L-tagatose"
---

# L-Fuculose

`molecule.C01721`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01721`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Fuculose; 6-Deoxy-L-tagatose

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Annotation

KEGG compound: L-Fuculose; 6-Deoxy-L-tagatose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R03163|reaction.R03163]] `KEGG` `database` - C01019 <=> C01721
- `is_product_of` --> [[reaction.ecocyc.FUCISOM-RXN|reaction.ecocyc.FUCISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.FUCULOKIN-RXN|reaction.ecocyc.FUCULOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01721`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
