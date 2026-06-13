---
entity_id: "molecule.C06510"
entity_type: "small_molecule"
name: "Adenosine-GDP-cobinamide"
source_database: "KEGG"
source_id: "C06510"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Adenosine-GDP-cobinamide"
  - "Adenosylcobinamide-GDP"
---

# Adenosine-GDP-cobinamide

`molecule.C06510`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06510`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Adenosine-GDP-cobinamide; Adenosylcobinamide-GDP EcoCyc common name: adenosylcobinamide-GDP.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Adenosine-GDP-cobinamide; Adenosylcobinamide-GDP

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R05223|reaction.R05223]] `KEGG` `database` - C00194 + C00144 <=> C06510 + C05775
- `is_product_of` --> [[reaction.ecocyc.COBINPGUANYLYLTRANS-RXN|reaction.ecocyc.COBINPGUANYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.COBALAMIN5PSYN-RXN|reaction.ecocyc.COBALAMIN5PSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06510`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
