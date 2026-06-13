---
entity_id: "molecule.C00136"
entity_type: "small_molecule"
name: "Butanoyl-CoA"
source_database: "KEGG"
source_id: "C00136"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Butanoyl-CoA"
  - "Butyryl-CoA"
---

# Butanoyl-CoA

`molecule.C00136`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00136`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Butanoyl-CoA; Butyryl-CoA

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)

## Annotation

KEGG compound: Butanoyl-CoA; Butyryl-CoA

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.BUTYRYL-COA-DEHYDROGENASE-RXN|reaction.ecocyc.BUTYRYL-COA-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12565|reaction.ecocyc.RXN-12565]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00136`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
