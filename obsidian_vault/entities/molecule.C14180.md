---
entity_id: "molecule.C14180"
entity_type: "small_molecule"
name: "S-(Hydroxymethyl)glutathione"
source_database: "KEGG"
source_id: "C14180"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "S-(Hydroxymethyl)glutathione"
---

# S-(Hydroxymethyl)glutathione

`molecule.C14180`

## Static

- Type: `small_molecule`
- Source: `KEGG:C14180`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: S-(Hydroxymethyl)glutathione

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: S-(Hydroxymethyl)glutathione

## Pathways

- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R06983|reaction.R06983]] `KEGG` `database` - C14180 + C00003 <=> C01031 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN-2961|reaction.ecocyc.RXN-2961]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-2962|reaction.ecocyc.RXN-2962]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C14180`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
