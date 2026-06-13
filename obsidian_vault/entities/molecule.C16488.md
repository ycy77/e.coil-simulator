---
entity_id: "molecule.C16488"
entity_type: "small_molecule"
name: "Fructoselysine"
source_database: "KEGG"
source_id: "C16488"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Fructoselysine"
  - "N6-(D-Fructosyl)-L-lysine"
---

# Fructoselysine

`molecule.C16488`

## Static

- Type: `small_molecule`
- Source: `KEGG:C16488`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Fructoselysine; N6-(D-Fructosyl)-L-lysine EcoCyc common name: N6-(1-deoxy-D-fructos-1-yl)-L-lysine. FRUCTOSELYSINE is formed by the reaction of CPD-15374 with the ε-amine of lysine, followed by a spontaneous isomerization of the sugar, referred to as an Amadori rearrangement .

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Fructoselysine; N6-(D-Fructosyl)-L-lysine

## Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN-20898|reaction.ecocyc.RXN-20898]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-417|reaction.ecocyc.TRANS-RXN0-417]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4841|reaction.ecocyc.RXN0-4841]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-962|reaction.ecocyc.RXN0-962]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-417|reaction.ecocyc.TRANS-RXN0-417]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C16488`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
