---
entity_id: "molecule.C00154"
entity_type: "small_molecule"
name: "Palmitoyl-CoA"
source_database: "KEGG"
source_id: "C00154"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Palmitoyl-CoA"
  - "Hexadecanoyl-CoA"
---

# Palmitoyl-CoA

`molecule.C00154`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00154`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Palmitoyl-CoA; Hexadecanoyl-CoA PALMITATE Palmitate (palmitic acid) is one of the most common saturated fatty acids found in animals and plants. The compound was discovered by Edmond Fremy in 1840 in saponified palm oil, of which it is a major component, and was named "palmitique". It is the first fatty acid produced during lipogenesis (fatty acid synthesis). In cells PALMITATE is usually found in the form of Palmitoyl-ACPs palmitoyl-[acp], PALMITYL-COA or Palmitoyl-lipid "incorporated into lipids".

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

KEGG compound: Palmitoyl-CoA; Hexadecanoyl-CoA

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.RXN-9623|reaction.ecocyc.RXN-9623]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN|reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CITSYN-RXN|reaction.ecocyc.CITSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ENOYL-ACP-REDUCT-NADPH-RXN|reaction.ecocyc.ENOYL-ACP-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN|reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-9657|reaction.ecocyc.RXN-9657]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00154`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
