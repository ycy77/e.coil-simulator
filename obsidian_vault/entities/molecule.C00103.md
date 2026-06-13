---
entity_id: "molecule.C00103"
entity_type: "small_molecule"
name: "D-Glucose 1-phosphate"
source_database: "KEGG"
source_id: "C00103"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glucose 1-phosphate"
  - "alpha-D-Glucose 1-phosphate"
  - "Cori ester"
  - "D-Glucose alpha-1-phosphate"
---

# D-Glucose 1-phosphate

`molecule.C00103`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00103`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glucose 1-phosphate; alpha-D-Glucose 1-phosphate; Cori ester; D-Glucose alpha-1-phosphate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)

## Annotation

KEGG compound: D-Glucose 1-phosphate; alpha-D-Glucose 1-phosphate; Cori ester; D-Glucose alpha-1-phosphate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.R00287|reaction.R00287]] `KEGG` `database` - C00029 + C00001 <=> C00105 + C00103
- `is_product_of` --> [[reaction.R02111|reaction.R02111]] `KEGG` `database` - C00369 + C00009 <=> C00718 + C00103
- `is_product_of` --> [[reaction.R06185|reaction.R06185]] `KEGG` `database` - G10545 + C00009 <=> G10495 + C00103
- `is_product_of` --> [[reaction.R11959|reaction.R11959]] `KEGG` `database` - C19792 + C00009 <=> C00103 + C00258
- `is_substrate_of` --> [[reaction.R00289|reaction.R00289]] `KEGG` `database` - C00075 + C00103 <=> C00013 + C00029
- `is_substrate_of` --> [[reaction.R00304|reaction.R00304]] `KEGG` `database` - C00103 + C00001 <=> C00031 + C00009
- `is_substrate_of` --> [[reaction.R02328|reaction.R02328]] `KEGG` `database` - C00459 + C00103 <=> C00013 + C00842
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17330|reaction.ecocyc.RXN-17330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00103`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
