---
entity_id: "molecule.C03979"
entity_type: "small_molecule"
name: "2-Dehydro-3-deoxy-L-rhamnonate"
source_database: "KEGG"
source_id: "C03979"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Dehydro-3-deoxy-L-rhamnonate"
---

# 2-Dehydro-3-deoxy-L-rhamnonate

`molecule.C03979`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03979`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Dehydro-3-deoxy-L-rhamnonate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Annotation

KEGG compound: 2-Dehydro-3-deoxy-L-rhamnonate

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R03774|reaction.R03774]] `KEGG` `database` - C01934 <=> C03979 + C00001
- `is_product_of` --> [[reaction.ecocyc.L-RHAMNONATE-DEHYDRATASE-RXN|reaction.ecocyc.L-RHAMNONATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5433|reaction.ecocyc.RXN0-5433]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03979`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
