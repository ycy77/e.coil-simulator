---
entity_id: "molecule.C00507"
entity_type: "small_molecule"
name: "L-Rhamnose"
source_database: "KEGG"
source_id: "C00507"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Rhamnose"
  - "6-Deoxy-L-mannose"
  - "L-Mannomethylose"
  - "L-Rhamnopyranose"
---

# L-Rhamnose

`molecule.C00507`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00507`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Rhamnose; 6-Deoxy-L-mannose; L-Mannomethylose; L-Rhamnopyranose This compound class represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Annotation

KEGG compound: L-Rhamnose; 6-Deoxy-L-mannose; L-Mannomethylose; L-Rhamnopyranose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX-124|complex.ecocyc.CPLX-124]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER-47|complex.ecocyc.MONOMER-47]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-112|reaction.ecocyc.TRANS-RXN-112]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-285|reaction.ecocyc.RXN0-285]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-286|reaction.ecocyc.RXN0-286]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-112|reaction.ecocyc.TRANS-RXN-112]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P27125|protein.P27125]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00507`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
