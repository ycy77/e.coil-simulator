---
entity_id: "molecule.C00249"
entity_type: "small_molecule"
name: "Hexadecanoic acid"
source_database: "KEGG"
source_id: "C00249"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Hexadecanoic acid"
  - "Hexadecanoate"
  - "Hexadecylic acid"
  - "Palmitic acid"
  - "Palmitate"
  - "Cetylic acid"
---

# Hexadecanoic acid

`molecule.C00249`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00249`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Hexadecanoic acid; Hexadecanoate; Hexadecylic acid; Palmitic acid; Palmitate; Cetylic acid EcoCyc common name: palmitate. PALMITATE Palmitate (palmitic acid) is one of the most common saturated fatty acids found in animals and plants. The compound was discovered by Edmond Frémy in 1840 in saponified palm oil, of which it is a major component, and was named "palmitique". It is the first fatty acid produced during lipogenesis (fatty acid synthesis). In cells PALMITATE is usually found in the form of Palmitoyl-ACPs palmitoyl-[acp], PALMITYL-COA or Palmitoyl-lipid "incorporated into lipids".

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

KEGG compound: Hexadecanoic acid; Hexadecanoate; Hexadecylic acid; Palmitic acid; Palmitate; Cetylic acid

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Outgoing Edges (4)

- `activates` --> [[reaction.ecocyc.RXN-11496|reaction.ecocyc.RXN-11496]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN|reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-9549|reaction.ecocyc.RXN-9549]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9623|reaction.ecocyc.RXN-9623]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00249`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
