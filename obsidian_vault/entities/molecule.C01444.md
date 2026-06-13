---
entity_id: "molecule.C01444"
entity_type: "small_molecule"
name: "Oxamate"
source_database: "KEGG"
source_id: "C01444"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Oxamate"
  - "Oxamic acid"
  - "Oxalic monoamide"
---

# Oxamate

`molecule.C01444`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01444`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Oxamate; Oxamic acid; Oxalic monoamide

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: Oxamate; Oxamic acid; Oxalic monoamide

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN|reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DLACTDEHYDROGFAD-RXN|reaction.ecocyc.DLACTDEHYDROGFAD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DLACTDEHYDROGNAD-RXN|reaction.ecocyc.DLACTDEHYDROGNAD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01444`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
