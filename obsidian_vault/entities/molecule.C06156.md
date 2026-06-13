---
entity_id: "molecule.C06156"
entity_type: "small_molecule"
name: "alpha-D-Glucosamine 1-phosphate"
source_database: "KEGG"
source_id: "C06156"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha-D-Glucosamine 1-phosphate"
  - "D-Glucosamine 1-phosphate"
---

# alpha-D-Glucosamine 1-phosphate

`molecule.C06156`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06156`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha-D-Glucosamine 1-phosphate; D-Glucosamine 1-phosphate EcoCyc common name: α-D-glucosamine 1-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Annotation

KEGG compound: alpha-D-Glucosamine 1-phosphate; D-Glucosamine 1-phosphate

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.5.4.2.10-RXN|reaction.ecocyc.5.4.2.10-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7139|reaction.ecocyc.RXN0-7139]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R05332|reaction.R05332]] `KEGG` `database` - C00024 + C06156 <=> C00010 + C04501
- `is_substrate_of` --> [[reaction.ecocyc.2.3.1.157-RXN|reaction.ecocyc.2.3.1.157-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06156`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
