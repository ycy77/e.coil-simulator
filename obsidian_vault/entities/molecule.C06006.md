---
entity_id: "molecule.C06006"
entity_type: "small_molecule"
name: "(S)-2-Aceto-2-hydroxybutanoate"
source_database: "KEGG"
source_id: "C06006"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-2-Aceto-2-hydroxybutanoate"
  - "(S)-2-Hydroxy-2-ethyl-3-oxobutanoate"
  - "(2S)-2-Ethyl-2-hydroxy-3-oxobutanoic acid"
---

# (S)-2-Aceto-2-hydroxybutanoate

`molecule.C06006`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06006`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-2-Aceto-2-hydroxybutanoate; (S)-2-Hydroxy-2-ethyl-3-oxobutanoate; (2S)-2-Ethyl-2-hydroxy-3-oxobutanoic acid

## Biological Role

Produced in 3 reaction(s).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)

## Annotation

KEGG compound: (S)-2-Aceto-2-hydroxybutanoate; (S)-2-Hydroxy-2-ethyl-3-oxobutanoate; (2S)-2-Ethyl-2-hydroxy-3-oxobutanoic acid

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R04673|reaction.R04673]] `KEGG` `database` - C00109 + C05125 <=> C06006 + C00068
- `is_product_of` --> [[reaction.ecocyc.ACETOOHBUTREDUCTOISOM-RXN|reaction.ecocyc.ACETOOHBUTREDUCTOISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETOOHBUTSYN-RXN|reaction.ecocyc.ACETOOHBUTSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06006`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
