---
entity_id: "molecule.C00679"
entity_type: "small_molecule"
name: "5-Dehydro-4-deoxy-D-glucarate"
source_database: "KEGG"
source_id: "C00679"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Dehydro-4-deoxy-D-glucarate"
  - "(2R,3S)-2,3-Dihydroxy-5-oxohexanedioate"
---

# 5-Dehydro-4-deoxy-D-glucarate

`molecule.C00679`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00679`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Dehydro-4-deoxy-D-glucarate; (2R,3S)-2,3-Dihydroxy-5-oxohexanedioate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: 5-Dehydro-4-deoxy-D-glucarate; (2R,3S)-2,3-Dihydroxy-5-oxohexanedioate

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.GALACTARDEHYDRA-RXN|reaction.ecocyc.GALACTARDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUCARDEHYDRA-RXN|reaction.ecocyc.GLUCARDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.KDGALDOL-RXN|reaction.ecocyc.KDGALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00679`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
