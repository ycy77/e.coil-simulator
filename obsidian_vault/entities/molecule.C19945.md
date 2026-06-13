---
entity_id: "molecule.C19945"
entity_type: "small_molecule"
name: "3-Oxo-5,6-dehydrosuberyl-CoA"
source_database: "KEGG"
source_id: "C19945"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Oxo-5,6-dehydrosuberyl-CoA"
  - "3-Oxo-5,6-didehydrosuberoyl-CoA"
---

# 3-Oxo-5,6-dehydrosuberyl-CoA

`molecule.C19945`

## Static

- Type: `small_molecule`
- Source: `KEGG:C19945`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Oxo-5,6-dehydrosuberyl-CoA; 3-Oxo-5,6-didehydrosuberoyl-CoA EcoCyc common name: 3-oxo-5,6-didehydrosuberyl-CoA.

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Annotation

KEGG compound: 3-Oxo-5,6-dehydrosuberyl-CoA; 3-Oxo-5,6-didehydrosuberoyl-CoA

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R09820|reaction.R09820]] `KEGG` `database` - C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.RXN0-6511|reaction.ecocyc.RXN0-6511]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6512|reaction.ecocyc.RXN0-6512]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXNMETA-12672|reaction.ecocyc.RXNMETA-12672]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C19945`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
