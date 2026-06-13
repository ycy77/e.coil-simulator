---
entity_id: "molecule.C03733"
entity_type: "small_molecule"
name: "UDP-alpha-D-galactofuranose"
source_database: "KEGG"
source_id: "C03733"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-alpha-D-galactofuranose"
  - "UDP-alpha-D-galacto-1,4-furanose"
  - "UDP-D-galacto-1,4-furanose"
---

# UDP-alpha-D-galactofuranose

`molecule.C03733`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03733`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-alpha-D-galactofuranose; UDP-alpha-D-galacto-1,4-furanose; UDP-D-galacto-1,4-furanose EcoCyc common name: UDP-α-D-galactofuranose.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: UDP-alpha-D-galactofuranose; UDP-alpha-D-galacto-1,4-furanose; UDP-D-galacto-1,4-furanose

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R00505|reaction.R00505]] `KEGG` `database` - C00052 <=> C03733
- `is_product_of` --> [[reaction.ecocyc.GALPMUT-RXN|reaction.ecocyc.GALPMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5210|reaction.ecocyc.RXN0-5210]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03733`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
