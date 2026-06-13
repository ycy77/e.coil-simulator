---
entity_id: "molecule.C00831"
entity_type: "small_molecule"
name: "Pantetheine"
source_database: "KEGG"
source_id: "C00831"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pantetheine"
  - "(R)-Pantetheine"
---

# Pantetheine

`molecule.C00831`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00831`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pantetheine; (R)-Pantetheine

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: Pantetheine; (R)-Pantetheine

## Pathways

- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.PANTETHEINE-KINASE-RXN|reaction.ecocyc.PANTETHEINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN|reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00831`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
