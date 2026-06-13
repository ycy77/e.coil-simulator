---
entity_id: "molecule.C00798"
entity_type: "small_molecule"
name: "Formyl-CoA"
source_database: "KEGG"
source_id: "C00798"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Formyl-CoA"
---

# Formyl-CoA

`molecule.C00798`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00798`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Formyl-CoA

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: Formyl-CoA

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R01908|reaction.R01908]] `KEGG` `database` - C00313 <=> C00798 + C00011
- `is_product_of` --> [[reaction.ecocyc.OXALYL-COA-DECARBOXYLASE-RXN|reaction.ecocyc.OXALYL-COA-DECARBOXYLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R07290|reaction.R07290]] `KEGG` `database` - C00798 + C00209 <=> C00058 + C00313
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1382|reaction.ecocyc.RXN0-1382]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00798`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
