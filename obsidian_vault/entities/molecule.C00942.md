---
entity_id: "molecule.C00942"
entity_type: "small_molecule"
name: "3',5'-Cyclic GMP"
source_database: "KEGG"
source_id: "C00942"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3',5'-Cyclic GMP"
  - "Guanosine 3',5'-cyclic monophosphate"
  - "Guanosine 3',5'-cyclic phosphate"
  - "Cyclic GMP"
  - "cGMP"
---

# 3',5'-Cyclic GMP

`molecule.C00942`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00942`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3',5'-Cyclic GMP; Guanosine 3',5'-cyclic monophosphate; Guanosine 3',5'-cyclic phosphate; Cyclic GMP; cGMP Like the better known CAMP, cGMP acts as a second messenger. In eukaryotes it regulates vasodilation through relaxation of smooth muscle tissue and also functions in the vertebrate visual system . Its role in prokaryotes is less well understood, though growing evidence suggests that it serves as a second messenger in bacteria as well .

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: 3',5'-Cyclic GMP; Guanosine 3',5'-cyclic monophosphate; Guanosine 3',5'-cyclic phosphate; Cyclic GMP; cGMP

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R00434|reaction.R00434]] `KEGG` `database` - C00044 <=> C00942 + C00013
- `is_product_of` --> [[reaction.ecocyc.GUANYLCYC-RXN|reaction.ecocyc.GUANYLCYC-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00942`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
