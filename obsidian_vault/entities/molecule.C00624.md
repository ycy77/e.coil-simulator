---
entity_id: "molecule.C00624"
entity_type: "small_molecule"
name: "N-Acetyl-L-glutamate"
source_database: "KEGG"
source_id: "C00624"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetyl-L-glutamate"
  - "N-Acetyl-L-glutamic acid"
---

# N-Acetyl-L-glutamate

`molecule.C00624`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00624`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetyl-L-glutamate; N-Acetyl-L-glutamic acid

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: N-Acetyl-L-glutamate; N-Acetyl-L-glutamic acid

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R00259|reaction.R00259]] `KEGG` `database` - C00024 + C00025 <=> C00010 + C00624
- `is_product_of` --> [[reaction.R13097|reaction.R13097]] `KEGG` `database` - C22611 <=> C00624
- `is_product_of` --> [[reaction.ecocyc.N-ACETYLTRANSFER-RXN|reaction.ecocyc.N-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ACETYLGLUTKIN-RXN|reaction.ecocyc.ACETYLGLUTKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00624`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
