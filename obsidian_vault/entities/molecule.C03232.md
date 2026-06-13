---
entity_id: "molecule.C03232"
entity_type: "small_molecule"
name: "3-Phosphonooxypyruvate"
source_database: "KEGG"
source_id: "C03232"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Phosphonooxypyruvate"
  - "3-Phosphonooxypyruvic acid"
  - "3-Phosphohydroxypyruvate"
  - "3-Phosphohydroxypyruvic acid"
  - "3-Phosphooxypyruvate"
---

# 3-Phosphonooxypyruvate

`molecule.C03232`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03232`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Phosphonooxypyruvate; 3-Phosphonooxypyruvic acid; 3-Phosphohydroxypyruvate; 3-Phosphohydroxypyruvic acid; 3-Phosphooxypyruvate EcoCyc common name: 3-phosphooxypyruvate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: 3-Phosphonooxypyruvate; 3-Phosphonooxypyruvic acid; 3-Phosphohydroxypyruvate; 3-Phosphohydroxypyruvic acid; 3-Phosphooxypyruvate

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.PGLYCDEHYDROG-RXN|reaction.ecocyc.PGLYCDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PSERTRANSAM-RXN|reaction.ecocyc.PSERTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6562|reaction.ecocyc.RXN0-6562]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KETOGLUTREDUCT-RXN|reaction.ecocyc.KETOGLUTREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-16701|reaction.ecocyc.RXN-16701]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03232`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
