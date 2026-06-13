---
entity_id: "molecule.C00341"
entity_type: "small_molecule"
name: "Geranyl diphosphate"
source_database: "KEGG"
source_id: "C00341"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Geranyl diphosphate"
---

# Geranyl diphosphate

`molecule.C00341`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00341`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Geranyl diphosphate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Annotation

KEGG compound: Geranyl diphosphate

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.GPPSYN-RXN|reaction.ecocyc.GPPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.FPPSYN-RXN|reaction.ecocyc.FPPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17104|reaction.ecocyc.RXN-17104]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20755|reaction.ecocyc.RXN-20755]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2281|reaction.ecocyc.RXN0-2281]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00341`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
