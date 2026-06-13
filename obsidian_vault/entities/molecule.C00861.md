---
entity_id: "molecule.C00861"
entity_type: "small_molecule"
name: "L-Rhamnulose"
source_database: "KEGG"
source_id: "C00861"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Rhamnulose"
  - "6-Deoxy-L-fructose"
---

# L-Rhamnulose

`molecule.C00861`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00861`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Rhamnulose; 6-Deoxy-L-fructose This compound class represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration. EcoCyc common name: keto-L-rhamnulose.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Annotation

KEGG compound: L-Rhamnulose; 6-Deoxy-L-fructose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RHAMNISOM-RXN|reaction.ecocyc.RHAMNISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15356|reaction.ecocyc.RXN-15356]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00861`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
