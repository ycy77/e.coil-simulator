---
entity_id: "molecule.C01934"
entity_type: "small_molecule"
name: "L-Rhamnonate"
source_database: "KEGG"
source_id: "C01934"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Rhamnonate"
  - "6-Deoxy-L-mannonic acid"
---

# L-Rhamnonate

`molecule.C01934`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01934`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Rhamnonate; 6-Deoxy-L-mannonic acid

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Annotation

KEGG compound: L-Rhamnonate; 6-Deoxy-L-mannonic acid

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R03774|reaction.R03774]] `KEGG` `database` - C01934 <=> C03979 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.L-RHAMNONATE-DEHYDRATASE-RXN|reaction.ecocyc.L-RHAMNONATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01934`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
