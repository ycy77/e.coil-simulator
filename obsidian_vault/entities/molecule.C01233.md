---
entity_id: "molecule.C01233"
entity_type: "small_molecule"
name: "sn-Glycero-3-phosphoethanolamine"
source_database: "KEGG"
source_id: "C01233"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "sn-Glycero-3-phosphoethanolamine"
  - "Glycerophosphoethanolamine"
---

# sn-Glycero-3-phosphoethanolamine

`molecule.C01233`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01233`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: sn-Glycero-3-phosphoethanolamine; Glycerophosphoethanolamine

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00565` Ether lipid metabolism (KEGG)

## Annotation

KEGG compound: sn-Glycero-3-phosphoethanolamine; Glycerophosphoethanolamine

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00565` Ether lipid metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R03416|reaction.R03416]] `KEGG` `database` - C04438 + C00001 <=> C00162 + C01233
- `is_product_of` --> [[reaction.R03417|reaction.R03417]] `KEGG` `database` - C05973 + C00001 <=> C00162 + C01233
- `is_product_of` --> [[reaction.ecocyc.RXN-19311|reaction.ecocyc.RXN-19311]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19312|reaction.ecocyc.RXN-19312]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7122|reaction.ecocyc.RXN0-7122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14160|reaction.ecocyc.RXN-14160]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01233`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
