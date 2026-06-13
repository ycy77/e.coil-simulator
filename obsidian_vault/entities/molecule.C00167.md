---
entity_id: "molecule.C00167"
entity_type: "small_molecule"
name: "UDP-glucuronate"
source_database: "KEGG"
source_id: "C00167"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-glucuronate"
  - "UDPglucuronate"
  - "UDP-D-glucuronate"
  - "UDP-alpha-D-glucuronate"
---

# UDP-glucuronate

`molecule.C00167`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00167`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-glucuronate; UDPglucuronate; UDP-D-glucuronate; UDP-alpha-D-glucuronate EcoCyc common name: UDP-α-D-glucuronate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: UDP-glucuronate; UDPglucuronate; UDP-D-glucuronate; UDP-alpha-D-glucuronate

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00286|reaction.R00286]] `KEGG` `database` - C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080
- `is_product_of` --> [[reaction.ecocyc.UGD-RXN|reaction.ecocyc.UGD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14361|reaction.ecocyc.RXN-14361]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22216|reaction.ecocyc.RXN-22216]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1861|reaction.ecocyc.RXN0-1861]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00167`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
