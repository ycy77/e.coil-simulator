---
entity_id: "molecule.C01170"
entity_type: "small_molecule"
name: "UDP-N-acetyl-D-mannosamine"
source_database: "KEGG"
source_id: "C01170"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-N-acetyl-D-mannosamine"
  - "UDP-N-acetyl-alpha-D-mannosamine"
---

# UDP-N-acetyl-D-mannosamine

`molecule.C01170`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01170`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-N-acetyl-D-mannosamine; UDP-N-acetyl-alpha-D-mannosamine EcoCyc common name: UDP-N-acetyl-α-D-mannosamine.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: UDP-N-acetyl-D-mannosamine; UDP-N-acetyl-alpha-D-mannosamine

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R00420|reaction.R00420]] `KEGG` `database` - C00043 <=> C01170
- `is_product_of` --> [[reaction.ecocyc.UDPGLCNACEPIM-RXN|reaction.ecocyc.UDPGLCNACEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.UDPMANNACADEHYDROG-RXN|reaction.ecocyc.UDPMANNACADEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01170`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
