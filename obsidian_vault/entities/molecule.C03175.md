---
entity_id: "molecule.C03175"
entity_type: "small_molecule"
name: "Shikimate 3-phosphate"
source_database: "KEGG"
source_id: "C03175"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Shikimate 3-phosphate"
  - "Shikimate 5-phosphate"
---

# Shikimate 3-phosphate

`molecule.C03175`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03175`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Shikimate 3-phosphate; Shikimate 5-phosphate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Annotation

KEGG compound: Shikimate 3-phosphate; Shikimate 5-phosphate

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.SHIKIMATE-KINASE-RXN|reaction.ecocyc.SHIKIMATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.2.5.1.19-RXN|reaction.ecocyc.2.5.1.19-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03175`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
