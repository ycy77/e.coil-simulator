---
entity_id: "molecule.C00689"
entity_type: "small_molecule"
name: "alpha,alpha'-Trehalose 6-phosphate"
source_database: "KEGG"
source_id: "C00689"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha,alpha'-Trehalose 6-phosphate"
  - "Trehalose 6-phosphate"
---

# alpha,alpha'-Trehalose 6-phosphate

`molecule.C00689`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00689`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha,alpha'-Trehalose 6-phosphate; Trehalose 6-phosphate EcoCyc common name: α,α-trehalose 6-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: alpha,alpha'-Trehalose 6-phosphate; Trehalose 6-phosphate

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R00836|reaction.R00836]] `KEGG` `database` - C00029 + C00092 <=> C00015 + C00689
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-168|reaction.ecocyc.TRANS-RXN-168]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TREHALOSE6PSYN-RXN|reaction.ecocyc.TREHALOSE6PSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00837|reaction.R00837]] `KEGG` `database` - C00001 + C00689 <=> C00031 + C00092
- `is_substrate_of` --> [[reaction.ecocyc.TRE6PHYDRO-RXN|reaction.ecocyc.TRE6PHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TREHALOSEPHOSPHA-RXN|reaction.ecocyc.TREHALOSEPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00689`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
