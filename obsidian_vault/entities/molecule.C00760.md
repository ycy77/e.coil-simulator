---
entity_id: "molecule.C00760"
entity_type: "small_molecule"
name: "Cellulose"
source_database: "KEGG"
source_id: "C00760"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cellulose"
  - "(1,4-beta-D-Glucosyl)n"
  - "(1,4-beta-D-Glucosyl)n+1"
  - "(1,4-beta-D-Glucosyl)n-1"
  - "1,4-beta-D-Glucan"
  - "Microcrystalline cellulose"
  - "(1,4-β-D-glucosyl)n"
---

# Cellulose

`molecule.C00760`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00760`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cellulose; (1,4-beta-D-Glucosyl)n; (1,4-beta-D-Glucosyl)n+1; (1,4-beta-D-Glucosyl)n-1; 1,4-beta-D-Glucan; Microcrystalline cellulose

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

KEGG compound: Cellulose; (1,4-beta-D-Glucosyl)n; (1,4-beta-D-Glucosyl)n+1; (1,4-beta-D-Glucosyl)n-1; 1,4-beta-D-Glucan; Microcrystalline cellulose

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R02889|reaction.R02889]] `KEGG` `database` - C00029 + C00760 <=> C00015 + C00760
- `is_product_of` --> [[reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN|reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02889|reaction.R02889]] `KEGG` `database` - C00029 + C00760 <=> C00015 + C00760
- `is_substrate_of` --> [[reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN|reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19630|reaction.ecocyc.RXN-19630]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-2043|reaction.ecocyc.RXN-2043]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00760`
- `EcoCyc:CELLULOSE`
- `canonicalized_from:molecule.ecocyc.CELLULOSE`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CELLULOSE: EcoCyc:CELLULOSE
