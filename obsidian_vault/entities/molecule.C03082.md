---
entity_id: "molecule.C03082"
entity_type: "small_molecule"
name: "4-Phospho-L-aspartate"
source_database: "KEGG"
source_id: "C03082"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Phospho-L-aspartate"
  - "L-4-Aspartyl phosphate"
---

# 4-Phospho-L-aspartate

`molecule.C03082`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03082`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Phospho-L-aspartate; L-4-Aspartyl phosphate EcoCyc common name: L-aspartyl-4-phosphate.

## Biological Role

Produced in 3 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)

## Annotation

KEGG compound: 4-Phospho-L-aspartate; L-4-Aspartyl phosphate

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R00480|reaction.R00480]] `KEGG` `database` - C00002 + C00049 <=> C00008 + C03082
- `is_product_of` --> [[reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ASPARTATEKIN-RXN|reaction.ecocyc.ASPARTATEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03082`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
