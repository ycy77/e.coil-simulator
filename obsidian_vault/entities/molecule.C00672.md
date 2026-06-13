---
entity_id: "molecule.C00672"
entity_type: "small_molecule"
name: "2-Deoxy-D-ribose 1-phosphate"
source_database: "KEGG"
source_id: "C00672"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Deoxy-D-ribose 1-phosphate"
  - "2-Deoxy-alpha-D-ribose 1-phosphate"
---

# 2-Deoxy-D-ribose 1-phosphate

`molecule.C00672`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00672`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Deoxy-D-ribose 1-phosphate; 2-Deoxy-alpha-D-ribose 1-phosphate EcoCyc common name: 2-deoxy-α-D-ribose 1-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: 2-Deoxy-D-ribose 1-phosphate; 2-Deoxy-alpha-D-ribose 1-phosphate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.R10244|reaction.R10244]] `KEGG` `database` - C20463 + C00009 <=> C15587 + C00672
- `is_product_of` --> [[reaction.ecocyc.DEOXYADENPHOSPHOR-RXN|reaction.ecocyc.DEOXYADENPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN|reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DEOXYINOPHOSPHOR-RXN|reaction.ecocyc.DEOXYINOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THYM-PHOSPH-RXN|reaction.ecocyc.THYM-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URA-PHOSPH-RXN|reaction.ecocyc.URA-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R08230|reaction.R08230]] `KEGG` `database` - C07649 + C00672 <=> C11736 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.D-PPENTOMUT-RXN|reaction.ecocyc.D-PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00672`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
