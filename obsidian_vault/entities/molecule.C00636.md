---
entity_id: "molecule.C00636"
entity_type: "small_molecule"
name: "D-Mannose 1-phosphate"
source_database: "KEGG"
source_id: "C00636"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Mannose 1-phosphate"
  - "alpha-D-Mannose 1-phosphate"
---

# D-Mannose 1-phosphate

`molecule.C00636`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00636`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Mannose 1-phosphate; alpha-D-Mannose 1-phosphate EcoCyc common name: α-D-mannose 1-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: D-Mannose 1-phosphate; alpha-D-Mannose 1-phosphate

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN0-5108|reaction.ecocyc.RXN0-5108]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.2.7.7.13-RXN|reaction.ecocyc.2.7.7.13-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHOSMANMUT-RXN|reaction.ecocyc.PHOSMANMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17725|reaction.ecocyc.RXN-17725]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00636`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
