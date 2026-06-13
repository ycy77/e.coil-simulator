---
entity_id: "molecule.C04534"
entity_type: "small_molecule"
name: "6-Phospho-beta-D-glucosyl-(1,4)-D-glucose"
source_database: "KEGG"
source_id: "C04534"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "6-Phospho-beta-D-glucosyl-(1,4)-D-glucose"
  - "Cellobiose 6'-phosphate"
  - "Cellobiose 6-phosphate"
---

# 6-Phospho-beta-D-glucosyl-(1,4)-D-glucose

`molecule.C04534`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04534`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 6-Phospho-beta-D-glucosyl-(1,4)-D-glucose; Cellobiose 6'-phosphate; Cellobiose 6-phosphate EcoCyc common name: β-D-cellobiose 6'-phosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: 6-Phospho-beta-D-glucosyl-(1,4)-D-glucose; Cellobiose 6'-phosphate; Cellobiose 6-phosphate

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-155|reaction.ecocyc.TRANS-RXN-155]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00839|reaction.R00839]] `KEGG` `database` - C04534 + C00001 <=> C00031 + C00092

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04534`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
