---
entity_id: "molecule.C00168"
entity_type: "small_molecule"
name: "Hydroxypyruvate"
source_database: "KEGG"
source_id: "C00168"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Hydroxypyruvate"
  - "Hydroxypyruvic acid"
  - "3-Hydroxypyruvate"
  - "3-Hydroxypyruvic acid"
---

# Hydroxypyruvate

`molecule.C00168`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00168`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Hydroxypyruvate; Hydroxypyruvic acid; 3-Hydroxypyruvate; 3-Hydroxypyruvic acid EcoCyc common name: 3-hydroxypyruvate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: Hydroxypyruvate; Hydroxypyruvic acid; 3-Hydroxypyruvate; 3-Hydroxypyruvic acid

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.RXN0-300|reaction.ecocyc.RXN0-300]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6562|reaction.ecocyc.RXN0-6562]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-305|reaction.ecocyc.RXN0-305]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DIHYDRODIPICSYN-RXN|reaction.ecocyc.DIHYDRODIPICSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYRUVDEH-RXN|reaction.ecocyc.PYRUVDEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-13990|reaction.ecocyc.RXN-13990]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7390|reaction.ecocyc.RXN0-7390]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00168`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
