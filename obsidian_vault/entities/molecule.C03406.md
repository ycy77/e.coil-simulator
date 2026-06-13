---
entity_id: "molecule.C03406"
entity_type: "small_molecule"
name: "N-(L-Arginino)succinate"
source_database: "KEGG"
source_id: "C03406"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-(L-Arginino)succinate"
  - "2-(Nomega-L-Arginino)succinate"
  - "L-Argininosuccinate"
  - "L-Argininosuccinic acid"
  - "L-Arginosuccinic acid"
---

# N-(L-Arginino)succinate

`molecule.C03406`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03406`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-(L-Arginino)succinate; 2-(Nomega-L-Arginino)succinate; L-Argininosuccinate; L-Argininosuccinic acid; L-Arginosuccinic acid EcoCyc common name: L-arginino-succinate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Annotation

KEGG compound: N-(L-Arginino)succinate; 2-(Nomega-L-Arginino)succinate; L-Argininosuccinate; L-Argininosuccinic acid; L-Arginosuccinic acid

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.ARGSUCCINSYN-RXN|reaction.ecocyc.ARGSUCCINSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ARGSUCCINLYA-RXN|reaction.ecocyc.ARGSUCCINLYA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03406`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
