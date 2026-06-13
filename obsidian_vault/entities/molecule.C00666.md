---
entity_id: "molecule.C00666"
entity_type: "small_molecule"
name: "LL-2,6-Diaminoheptanedioate"
source_database: "KEGG"
source_id: "C00666"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "LL-2,6-Diaminoheptanedioate"
  - "LL-2,6-Diaminopimelate"
  - "LL-2,6-Diaminopimelic acid"
  - "(2S,6S)-2,6-Diaminoheptanedioic acid"
---

# LL-2,6-Diaminoheptanedioate

`molecule.C00666`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00666`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: LL-2,6-Diaminoheptanedioate; LL-2,6-Diaminopimelate; LL-2,6-Diaminopimelic acid; (2S,6S)-2,6-Diaminoheptanedioic acid EcoCyc common name: L,L-diaminopimelate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: LL-2,6-Diaminoheptanedioate; LL-2,6-Diaminopimelate; LL-2,6-Diaminopimelic acid; (2S,6S)-2,6-Diaminoheptanedioic acid

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.SUCCDIAMINOPIMDESUCC-RXN|reaction.ecocyc.SUCCDIAMINOPIMDESUCC-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DIAMINOPIMEPIM-RXN|reaction.ecocyc.DIAMINOPIMEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00666`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
