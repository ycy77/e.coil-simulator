---
entity_id: "molecule.C01179"
entity_type: "small_molecule"
name: "3-(4-Hydroxyphenyl)pyruvate"
source_database: "KEGG"
source_id: "C01179"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-(4-Hydroxyphenyl)pyruvate"
  - "4-Hydroxyphenylpyruvate"
  - "p-Hydroxyphenylpyruvic acid"
---

# 3-(4-Hydroxyphenyl)pyruvate

`molecule.C01179`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01179`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-(4-Hydroxyphenyl)pyruvate; 4-Hydroxyphenylpyruvate; p-Hydroxyphenylpyruvic acid

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)

## Annotation

KEGG compound: 3-(4-Hydroxyphenyl)pyruvate; 4-Hydroxyphenylpyruvate; p-Hydroxyphenylpyruvic acid

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R00734|reaction.R00734]] `KEGG` `database` - C00082 + C00026 <=> C01179 + C00025
- `is_product_of` --> [[reaction.R01728|reaction.R01728]] `KEGG` `database` - C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.PREPHENATEDEHYDROG-RXN|reaction.ecocyc.PREPHENATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01179`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
