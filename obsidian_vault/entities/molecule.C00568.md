---
entity_id: "molecule.C00568"
entity_type: "small_molecule"
name: "4-Aminobenzoate"
source_database: "KEGG"
source_id: "C00568"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Aminobenzoate"
  - "ABEE"
  - "4-Aminobenzoic acid"
  - "p-Aminobenzoate"
---

# 4-Aminobenzoate

`molecule.C00568`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00568`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Aminobenzoate; ABEE; 4-Aminobenzoic acid; p-Aminobenzoate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: 4-Aminobenzoate; ABEE; 4-Aminobenzoic acid; p-Aminobenzoate

## Pathways

- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.ADCLY-RXN|reaction.ecocyc.ADCLY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5040|reaction.ecocyc.RXN0-5040]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.H2PTEROATESYNTH-RXN|reaction.ecocyc.H2PTEROATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00568`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
