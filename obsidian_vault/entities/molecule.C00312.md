---
entity_id: "molecule.C00312"
entity_type: "small_molecule"
name: "L-Xylulose"
source_database: "KEGG"
source_id: "C00312"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Xylulose"
  - "L-threo-Pentulose"
  - "L-Lyxulose"
---

# L-Xylulose

`molecule.C00312`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00312`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Xylulose; L-threo-Pentulose; L-Lyxulose This compound class represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: L-Xylulose; L-threo-Pentulose; L-Lyxulose

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.LYXISOM-RXN|reaction.ecocyc.LYXISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01901|reaction.R01901]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C03291
- `is_substrate_of` --> [[reaction.R01902|reaction.R01902]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C06441
- `is_substrate_of` --> [[reaction.ecocyc.LYXK-RXN|reaction.ecocyc.LYXK-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00312`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
