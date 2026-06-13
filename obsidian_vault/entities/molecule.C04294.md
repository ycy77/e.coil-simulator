---
entity_id: "molecule.C04294"
entity_type: "small_molecule"
name: "5-(2-Hydroxyethyl)-4-methylthiazole"
source_database: "KEGG"
source_id: "C04294"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-(2-Hydroxyethyl)-4-methylthiazole"
  - "4-Methyl-5-(2'-hydroxyethyl)-thiazole"
  - "4-Methyl-5-(2-hydroxyethyl)thiazole"
  - "HET"
---

# 5-(2-Hydroxyethyl)-4-methylthiazole

`molecule.C04294`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04294`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-(2-Hydroxyethyl)-4-methylthiazole; 4-Methyl-5-(2'-hydroxyethyl)-thiazole; 4-Methyl-5-(2-hydroxyethyl)thiazole; HET

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Annotation

KEGG compound: 5-(2-Hydroxyethyl)-4-methylthiazole; 4-Methyl-5-(2'-hydroxyethyl)-thiazole; 4-Methyl-5-(2-hydroxyethyl)thiazole; HET

## Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-464|reaction.ecocyc.TRANS-RXN0-464]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.THIAZOLSYN3-RXN|reaction.ecocyc.THIAZOLSYN3-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-464|reaction.ecocyc.TRANS-RXN0-464]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04294`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
