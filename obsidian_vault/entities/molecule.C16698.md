---
entity_id: "molecule.C16698"
entity_type: "small_molecule"
name: "N-Acetylmuramic acid 6-phosphate"
source_database: "KEGG"
source_id: "C16698"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetylmuramic acid 6-phosphate"
  - "N-Acetylmuramate 6-phosphate"
  - "MurNAc 6-phosphate"
---

# N-Acetylmuramic acid 6-phosphate

`molecule.C16698`

## Static

- Type: `small_molecule`
- Source: `KEGG:C16698`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetylmuramic acid 6-phosphate; N-Acetylmuramate 6-phosphate; MurNAc 6-phosphate EcoCyc common name: N-acetyl-D-muramate 6-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: N-Acetylmuramic acid 6-phosphate; N-Acetylmuramate 6-phosphate; MurNAc 6-phosphate

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7746|complex.ecocyc.CPLX0-7746]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN0-17|reaction.ecocyc.RXN0-17]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-4621|reaction.ecocyc.RXN0-4621]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4641|reaction.ecocyc.RXN0-4641]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5465|reaction.ecocyc.RXN0-5465]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C16698`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
