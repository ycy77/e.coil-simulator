---
entity_id: "molecule.C03508"
entity_type: "small_molecule"
name: "L-2-Amino-3-oxobutanoic acid"
source_database: "KEGG"
source_id: "C03508"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-2-Amino-3-oxobutanoic acid"
  - "L-2-Amino-3-oxobutanoate"
  - "L-2-Amino-acetoacetate"
  - "(S)-2-Amino-3-oxobutanoic acid"
---

# L-2-Amino-3-oxobutanoic acid

`molecule.C03508`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03508`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-2-Amino-3-oxobutanoic acid; L-2-Amino-3-oxobutanoate; L-2-Amino-acetoacetate; (S)-2-Amino-3-oxobutanoic acid EcoCyc common name: L-2-amino-3-oxobutanoate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)

## Annotation

KEGG compound: L-2-Amino-3-oxobutanoic acid; L-2-Amino-3-oxobutanoate; L-2-Amino-acetoacetate; (S)-2-Amino-3-oxobutanoic acid

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R00371|reaction.R00371]] `KEGG` `database` - C00024 + C00037 <=> C00010 + C03508
- `is_product_of` --> [[reaction.R03758|reaction.R03758]] `KEGG` `database` - C01888 + C00011 <=> C03508
- `is_product_of` --> [[reaction.ecocyc.AKBLIG-RXN|reaction.ecocyc.AKBLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16000|reaction.ecocyc.RXN-16000]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THREODEHYD-RXN|reaction.ecocyc.THREODEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.THREOSPON-RXN|reaction.ecocyc.THREOSPON-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03508`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
