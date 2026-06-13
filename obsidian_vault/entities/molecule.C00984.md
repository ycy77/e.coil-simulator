---
entity_id: "molecule.C00984"
entity_type: "small_molecule"
name: "alpha-D-Galactose"
source_database: "KEGG"
source_id: "C00984"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha-D-Galactose"
---

# alpha-D-Galactose

`molecule.C00984`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00984`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha-D-Galactose EcoCyc common name: α-D-galactopyranose.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: alpha-D-Galactose

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.ALDOSE1EPIM-RXN|reaction.ecocyc.ALDOSE1EPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17754|reaction.ecocyc.RXN-17754]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GALACTOKIN-RXN|reaction.ecocyc.GALACTOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00984`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
