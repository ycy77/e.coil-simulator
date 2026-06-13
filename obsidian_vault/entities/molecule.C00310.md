---
entity_id: "molecule.C00310"
entity_type: "small_molecule"
name: "D-Xylulose"
source_database: "KEGG"
source_id: "C00310"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Xylulose"
  - "D-threo-Pentulose"
  - "D-Lyxulose"
---

# D-Xylulose

`molecule.C00310`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00310`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Xylulose; D-threo-Pentulose; D-Lyxulose This compound class represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: D-Xylulose; D-threo-Pentulose; D-Lyxulose

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R01896|reaction.R01896]] `KEGG` `database` - C00379 + C00003 <=> C00310 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.D-ARABINITOL-4-DEHYDROGENASE-RXN|reaction.ecocyc.D-ARABINITOL-4-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.D-XYLULOSE-REDUCTASE-RXN|reaction.ecocyc.D-XYLULOSE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-25603|reaction.ecocyc.RXN-25603]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.XYLULOKIN-RXN|reaction.ecocyc.XYLULOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00310`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
