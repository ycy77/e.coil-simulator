---
entity_id: "molecule.C01419"
entity_type: "small_molecule"
name: "Cys-Gly"
source_database: "KEGG"
source_id: "C01419"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cys-Gly"
  - "L-Cysteinylglycine"
---

# Cys-Gly

`molecule.C01419`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01419`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cys-Gly; L-Cysteinylglycine EcoCyc common name: L-cysteinylglycine.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)

## Annotation

KEGG compound: Cys-Gly; L-Cysteinylglycine

## Pathways

- `eco00480` Glutathione metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00494|reaction.R00494]] `KEGG` `database` - C00051 + C00001 <=> C01419 + C00025
- `is_product_of` --> [[reaction.ecocyc.RXN-12618|reaction.ecocyc.RXN-12618]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18092|reaction.ecocyc.RXN-18092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19024|reaction.ecocyc.RXN-19024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-6622|reaction.ecocyc.RXN-6622]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01419`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
