---
entity_id: "molecule.C06473"
entity_type: "small_molecule"
name: "2-Keto-D-gluconic acid"
source_database: "KEGG"
source_id: "C06473"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Keto-D-gluconic acid"
  - "2-Dehydro-D-gluconate"
  - "2-Dehydro-D-gluconic acid"
  - "alpha-D-arabino-2-Hexulosonic acid"
---

# 2-Keto-D-gluconic acid

`molecule.C06473`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06473`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Keto-D-gluconic acid; 2-Dehydro-D-gluconate; 2-Dehydro-D-gluconic acid; alpha-D-arabino-2-Hexulosonic acid EcoCyc common name: 2-keto-D-gluconate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Annotation

KEGG compound: 2-Keto-D-gluconic acid; 2-Dehydro-D-gluconate; 2-Dehydro-D-gluconic acid; alpha-D-arabino-2-Hexulosonic acid

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R01739|reaction.R01739]] `KEGG` `database` - C00257 + C00006 <=> C06473 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.1.1.1.215-RXN|reaction.ecocyc.1.1.1.215-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.274-RXN|reaction.ecocyc.1.1.1.274-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDGALDOL-RXN|reaction.ecocyc.KDGALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06473`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
