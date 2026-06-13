---
entity_id: "molecule.C00692"
entity_type: "small_molecule"
name: "UDP-N-acetylmuramoyl-L-alanyl-D-glutamate"
source_database: "KEGG"
source_id: "C00692"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-N-acetylmuramoyl-L-alanyl-D-glutamate"
  - "UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-D-glutamate"
---

# UDP-N-acetylmuramoyl-L-alanyl-D-glutamate

`molecule.C00692`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00692`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-N-acetylmuramoyl-L-alanyl-D-glutamate; UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-D-glutamate EcoCyc common name: UDP-N-acetyl-α-D-muramoyl-L-alanyl-D-glutamate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

KEGG compound: UDP-N-acetylmuramoyl-L-alanyl-D-glutamate; UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-D-glutamate

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN|reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02788|reaction.R02788]] `KEGG` `database` - C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877
- `is_substrate_of` --> [[reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN|reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00692`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
