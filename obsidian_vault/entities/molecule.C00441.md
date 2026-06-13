---
entity_id: "molecule.C00441"
entity_type: "small_molecule"
name: "L-Aspartate 4-semialdehyde"
source_database: "KEGG"
source_id: "C00441"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Aspartate 4-semialdehyde"
  - "Aspartate beta-semialdehyde"
  - "L-Aspartic 4-semialdehyde"
---

# L-Aspartate 4-semialdehyde

`molecule.C00441`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00441`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Aspartate 4-semialdehyde; Aspartate beta-semialdehyde; L-Aspartic 4-semialdehyde

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Annotation

KEGG compound: L-Aspartate 4-semialdehyde; Aspartate beta-semialdehyde; L-Aspartic 4-semialdehyde

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.HOMOSERDEHYDROG-RXN|reaction.ecocyc.HOMOSERDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDRODIPICSYN-RXN|reaction.ecocyc.DIHYDRODIPICSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ASPARTASE-RXN|reaction.ecocyc.ASPARTASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00441`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
