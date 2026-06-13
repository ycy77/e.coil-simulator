---
entity_id: "molecule.C00108"
entity_type: "small_molecule"
name: "Anthranilate"
source_database: "KEGG"
source_id: "C00108"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Anthranilate"
  - "Anthranilic acid"
  - "o-Aminobenzoic acid"
  - "Vitamin L1"
  - "2-Aminobenzoate"
---

# Anthranilate

`molecule.C00108`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00108`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Anthranilate; Anthranilic acid; o-Aminobenzoic acid; Vitamin L1; 2-Aminobenzoate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: Anthranilate; Anthranilic acid; o-Aminobenzoic acid; Vitamin L1; 2-Aminobenzoate

## Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.R00985|reaction.R00985]] `KEGG` `database` - C00251 + C00014 <=> C00108 + C00022 + C00001
- `is_product_of` --> [[reaction.R00986|reaction.R00986]] `KEGG` `database` - C00251 + C00064 <=> C00108 + C00022 + C00025
- `is_product_of` --> [[reaction.ecocyc.ANTHRANSYN-RXN|reaction.ecocyc.ANTHRANSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PRTRANS-RXN|reaction.ecocyc.PRTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22729|reaction.ecocyc.RXN-22729]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R12035|reaction.R12035]] `KEGG` `database` - C00108 + C04203 + 2 C00003 <=> C19459 + 2 C00004 + 2 C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5375|reaction.ecocyc.RXN0-5375]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.IGPSYN-RXN|reaction.ecocyc.IGPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00108`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
