---
entity_id: "molecule.C01879"
entity_type: "small_molecule"
name: "5-Oxoproline"
source_database: "KEGG"
source_id: "C01879"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Oxoproline"
  - "Pidolic acid"
  - "Pyroglutamic acid"
  - "5-Pyrrolidone-2-carboxylic acid"
  - "Pyroglutamate"
  - "5-Oxo-L-proline"
  - "L-Pyroglutamic acid"
  - "L-5-Pyrrolidone-2-carboxylic acid"
---

# 5-Oxoproline

`molecule.C01879`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01879`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Oxoproline; Pidolic acid; Pyroglutamic acid; 5-Pyrrolidone-2-carboxylic acid; Pyroglutamate; 5-Oxo-L-proline; L-Pyroglutamic acid; L-5-Pyrrolidone-2-carboxylic acid EcoCyc common name: 5-oxo-L-proline.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)

## Annotation

KEGG compound: 5-Oxoproline; Pidolic acid; Pyroglutamic acid; 5-Pyrrolidone-2-carboxylic acid; Pyroglutamate; 5-Oxo-L-proline; L-Pyroglutamic acid; L-5-Pyrrolidone-2-carboxylic acid

## Pathways

- `eco00480` Glutathione metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN-19022|reaction.ecocyc.RXN-19022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19024|reaction.ecocyc.RXN-19024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00251|reaction.R00251]] `KEGG` `database` - C00002 + C01879 + 2 C00001 <=> C00008 + C00009 + C00025
- `is_substrate_of` --> [[reaction.ecocyc.5-OXOPROLINASE-ATP-HYDROLYSING-RXN|reaction.ecocyc.5-OXOPROLINASE-ATP-HYDROLYSING-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01879`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
