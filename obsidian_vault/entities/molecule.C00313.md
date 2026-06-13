---
entity_id: "molecule.C00313"
entity_type: "small_molecule"
name: "Oxalyl-CoA"
source_database: "KEGG"
source_id: "C00313"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Oxalyl-CoA"
---

# Oxalyl-CoA

`molecule.C00313`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00313`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Oxalyl-CoA

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: Oxalyl-CoA

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R07290|reaction.R07290]] `KEGG` `database` - C00798 + C00209 <=> C00058 + C00313
- `is_product_of` --> [[reaction.ecocyc.RXN0-1382|reaction.ecocyc.RXN0-1382]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7075|reaction.ecocyc.RXN0-7075]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01908|reaction.R01908]] `KEGG` `database` - C00313 <=> C00798 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.OXALYL-COA-DECARBOXYLASE-RXN|reaction.ecocyc.OXALYL-COA-DECARBOXYLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00313`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
