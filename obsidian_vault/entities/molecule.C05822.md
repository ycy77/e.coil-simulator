---
entity_id: "molecule.C05822"
entity_type: "small_molecule"
name: "3'-CMP"
source_database: "KEGG"
source_id: "C05822"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3'-CMP"
  - "Cytidine 3'-phosphate"
---

# 3'-CMP

`molecule.C05822`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05822`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3'-CMP; Cytidine 3'-phosphate EcoCyc common name: cytidine-3'-monophosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: 3'-CMP; Cytidine 3'-phosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-14112|reaction.ecocyc.RXN-14112]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02370|reaction.R02370]] `KEGG` `database` - C05822 + C00001 <=> C00475 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14090|reaction.ecocyc.RXN-14090]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05822`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
