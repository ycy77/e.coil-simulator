---
entity_id: "molecule.C01236"
entity_type: "small_molecule"
name: "D-Glucono-1,5-lactone 6-phosphate"
source_database: "KEGG"
source_id: "C01236"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glucono-1,5-lactone 6-phosphate"
  - "6-Phospho-D-glucono-1,5-lactone"
---

# D-Glucono-1,5-lactone 6-phosphate

`molecule.C01236`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01236`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glucono-1,5-lactone 6-phosphate; 6-Phospho-D-glucono-1,5-lactone EcoCyc common name: 6-phospho D-glucono-1,5-lactone.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Annotation

KEGG compound: D-Glucono-1,5-lactone 6-phosphate; 6-Phospho-D-glucono-1,5-lactone

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R00835|reaction.R00835]] `KEGG` `database` - C00092 + C00006 <=> C01236 + C00005 + C00080
- `is_product_of` --> [[reaction.R10907|reaction.R10907]] `KEGG` `database` - C01172 + C00003 <=> C01236 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.GLU6PDEHYDROG-RXN|reaction.ecocyc.GLU6PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.6PGLUCONOLACT-RXN|reaction.ecocyc.6PGLUCONOLACT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01236`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
