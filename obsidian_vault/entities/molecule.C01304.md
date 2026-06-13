---
entity_id: "molecule.C01304"
entity_type: "small_molecule"
name: "2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one"
source_database: "KEGG"
source_id: "C01304"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one"
  - "2,5-Diamino-6-(1-D-ribosylamino)pyrimidin-4(3H)-one 5'-phosphate"
---

# 2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one

`molecule.C01304`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01304`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one; 2,5-Diamino-6-(1-D-ribosylamino)pyrimidin-4(3H)-one 5'-phosphate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: 2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one; 2,5-Diamino-6-(1-D-ribosylamino)pyrimidin-4(3H)-one 5'-phosphate

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R00425|reaction.R00425]] `KEGG` `database` - C00044 + 4 C00001 <=> C00058 + C01304 + 2 C00009
- `is_product_of` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RIBOFLAVINSYNDEAM-RXN|reaction.ecocyc.RIBOFLAVINSYNDEAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01304`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
