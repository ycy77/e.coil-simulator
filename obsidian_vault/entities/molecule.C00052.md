---
entity_id: "molecule.C00052"
entity_type: "small_molecule"
name: "UDP-alpha-D-galactose"
source_database: "KEGG"
source_id: "C00052"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-alpha-D-galactose"
  - "UDP-D-galactose"
  - "UDP-galactose"
  - "UDP-D-galactopyranose"
  - "UDP-alpha-D-galactopyranose"
---

# UDP-alpha-D-galactose

`molecule.C00052`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00052`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-alpha-D-galactose; UDP-D-galactose; UDP-galactose; UDP-D-galactopyranose; UDP-alpha-D-galactopyranose EcoCyc common name: UDP-α-D-galactose.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: UDP-alpha-D-galactose; UDP-D-galactose; UDP-galactose; UDP-D-galactopyranose; UDP-alpha-D-galactopyranose

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.R00291|reaction.R00291]] `KEGG` `database` - C00029 <=> C00052
- `is_product_of` --> [[reaction.ecocyc.GALACTURIDYLYLTRANS-RXN|reaction.ecocyc.GALACTURIDYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.UDPGLUCEPIM-RXN|reaction.ecocyc.UDPGLUCEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00505|reaction.R00505]] `KEGG` `database` - C00052 <=> C03733
- `is_substrate_of` --> [[reaction.ecocyc.GALPMUT-RXN|reaction.ecocyc.GALPMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22215|reaction.ecocyc.RXN-22215]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5124|reaction.ecocyc.RXN0-5124]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7344|reaction.ecocyc.RXN0-7344]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00052`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
