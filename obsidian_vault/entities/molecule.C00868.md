---
entity_id: "molecule.C00868"
entity_type: "small_molecule"
name: "tRNA uridine"
source_database: "KEGG"
source_id: "C00868"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "tRNA uridine"
  - "Uracil in tRNA"
---

# tRNA uridine

`molecule.C00868`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00868`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: tRNA uridine; Uracil in tRNA EcoCyc common name: a uridine in tRNA. This class describes a uridine residue within the context of a tRNA molecule.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

KEGG compound: tRNA uridine; Uracil in tRNA

## Pathways

- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN0-1281|reaction.ecocyc.RXN0-1281]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21179|reaction.ecocyc.RXN-21179]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00868`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
