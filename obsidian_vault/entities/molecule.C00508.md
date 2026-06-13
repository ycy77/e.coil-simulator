---
entity_id: "molecule.C00508"
entity_type: "small_molecule"
name: "L-Ribulose"
source_database: "KEGG"
source_id: "C00508"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Ribulose"
  - "L-erythro-Pentulose"
  - "L-Arabinoketose"
  - "L-Arabinulose"
  - "L-Riboketose"
---

# L-Ribulose

`molecule.C00508`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00508`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Ribulose; L-erythro-Pentulose; L-Arabinoketose; L-Arabinulose; L-Riboketose This compound class represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: L-Ribulose; L-erythro-Pentulose; L-Arabinoketose; L-Arabinulose; L-Riboketose

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.ARABISOM-RXN|reaction.ecocyc.ARABISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5116|reaction.ecocyc.RXN0-5116]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00508`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
