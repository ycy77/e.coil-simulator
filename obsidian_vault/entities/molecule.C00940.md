---
entity_id: "molecule.C00940"
entity_type: "small_molecule"
name: "2-Oxoglutaramate"
source_database: "KEGG"
source_id: "C00940"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Oxoglutaramate"
  - "2-Oxoglutaramic acid"
  - "alpha-Ketoglutaramate"
  - "2-Ketoglutaramate"
---

# 2-Oxoglutaramate

`molecule.C00940`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00940`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Oxoglutaramate; 2-Oxoglutaramic acid; alpha-Ketoglutaramate; 2-Ketoglutaramate

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Annotation

KEGG compound: 2-Oxoglutaramate; 2-Oxoglutaramic acid; alpha-Ketoglutaramate; 2-Ketoglutaramate

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R00269|reaction.R00269]] `KEGG` `database` - C00940 + C00001 <=> C00026 + C00014
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13072|reaction.ecocyc.RXN-13072]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00940`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
