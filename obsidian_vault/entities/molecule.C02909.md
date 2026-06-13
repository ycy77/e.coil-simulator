---
entity_id: "molecule.C02909"
entity_type: "small_molecule"
name: "(2-Naphthyl)methanol"
source_database: "KEGG"
source_id: "C02909"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(2-Naphthyl)methanol"
  - "2-Naphthalenemethanol"
  - "2-Hydroxymethylnaphthalene"
---

# (2-Naphthyl)methanol

`molecule.C02909`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02909`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (2-Naphthyl)methanol; 2-Naphthalenemethanol; 2-Hydroxymethylnaphthalene

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00626` Naphthalene degradation (KEGG)

## Annotation

KEGG compound: (2-Naphthyl)methanol; 2-Naphthalenemethanol; 2-Hydroxymethylnaphthalene

## Pathways

- `eco00626` Naphthalene degradation (KEGG)

## Outgoing Edges (1)

- `is_substrate_of` --> [[reaction.R06927|reaction.R06927]] `KEGG` `database` - C02909 + C00003 <=> C14099 + C00004 + C00080

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02909`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
