---
entity_id: "molecule.C00446"
entity_type: "small_molecule"
name: "alpha-D-Galactose 1-phosphate"
source_database: "KEGG"
source_id: "C00446"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha-D-Galactose 1-phosphate"
  - "alpha-D-Galactopyranose 1-phosphate"
---

# alpha-D-Galactose 1-phosphate

`molecule.C00446`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00446`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha-D-Galactose 1-phosphate; alpha-D-Galactopyranose 1-phosphate EcoCyc common name: α-D-galactose 1-phosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: alpha-D-Galactose 1-phosphate; alpha-D-Galactopyranose 1-phosphate

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.GALACTOKIN-RXN|reaction.ecocyc.GALACTOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GALACTURIDYLYLTRANS-RXN|reaction.ecocyc.GALACTURIDYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00446`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
