---
entity_id: "molecule.C01212"
entity_type: "small_molecule"
name: "UDP-N-acetylmuramoyl-L-alanine"
source_database: "KEGG"
source_id: "C01212"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-N-acetylmuramoyl-L-alanine"
  - "UDP-N-acetyl-alpha-D-muramoyl-L-alanine"
---

# UDP-N-acetylmuramoyl-L-alanine

`molecule.C01212`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01212`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-N-acetylmuramoyl-L-alanine; UDP-N-acetyl-alpha-D-muramoyl-L-alanine EcoCyc common name: UDP-N-acetyl-α-D-muramoyl-L-alanine.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

KEGG compound: UDP-N-acetylmuramoyl-L-alanine; UDP-N-acetyl-alpha-D-muramoyl-L-alanine

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Outgoing Edges (5)

- `activates` --> [[reaction.ecocyc.GLUTRACE-RXN|reaction.ecocyc.GLUTRACE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R03193|reaction.R03193]] `KEGG` `database` - C00002 + C01050 + C00041 <=> C00008 + C00009 + C01212
- `is_product_of` --> [[reaction.ecocyc.UDP-NACMUR-ALA-LIG-RXN|reaction.ecocyc.UDP-NACMUR-ALA-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN|reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01212`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
