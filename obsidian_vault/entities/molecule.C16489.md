---
entity_id: "molecule.C16489"
entity_type: "small_molecule"
name: "Fructoselysine 6-phosphate"
source_database: "KEGG"
source_id: "C16489"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Fructoselysine 6-phosphate"
---

# Fructoselysine 6-phosphate

`molecule.C16489`

## Static

- Type: `small_molecule`
- Source: `KEGG:C16489`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Fructoselysine 6-phosphate EcoCyc common name: N6-(1-deoxy-6-O-phospho-D-fructos-1-yl)-L-lysine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Fructoselysine 6-phosphate

## Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8577|complex.ecocyc.CPLX0-8577]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN0-962|reaction.ecocyc.RXN0-962]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7382|reaction.ecocyc.RXN0-7382]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-963|reaction.ecocyc.RXN0-963]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C16489`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
