---
entity_id: "molecule.C00255"
entity_type: "small_molecule"
name: "Riboflavin"
source_database: "KEGG"
source_id: "C00255"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Riboflavin"
  - "Lactoflavin"
  - "7,8-Dimethyl-10-ribitylisoalloxazine"
  - "Vitamin B2"
---

# Riboflavin

`molecule.C00255`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00255`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Riboflavin; Lactoflavin; 7,8-Dimethyl-10-ribitylisoalloxazine; Vitamin B2 RIBOFLAVIN Riboflavin is the precursor for the essential FLAVIN flavin cofactors FMN and FAD, which are used in a wide variety of redox reactions. Riboflavin is also known as vitamin B2, because it is an essential nutrient and can not be synthesized by mammals. The name riboflavin is derived from D-Ribose ribose (the sugar whose reduced form, RIBITOL, forms part of its structure) and FLAVIN flavin, the ring-moiety.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Riboflavin; Lactoflavin; 7,8-Dimethyl-10-ribitylisoalloxazine; Vitamin B2

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.R00066|reaction.R00066]] `KEGG` `database` - 2 C04332 <=> C00255 + C04732
- `is_product_of` --> [[reaction.R00548|reaction.R00548]] `KEGG` `database` - C00061 + C00001 <=> C00255 + C00009
- `is_product_of` --> [[reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN|reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBOFLAVIN-SYN-RXN|reaction.ecocyc.RIBOFLAVIN-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12445|reaction.ecocyc.RXN-12445]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5187|reaction.ecocyc.RXN0-5187]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00549|reaction.R00549]] `KEGG` `database` - C00002 + C00255 <=> C00008 + C00061
- `is_substrate_of` --> [[reaction.ecocyc.RIBOFLAVINKIN-RXN|reaction.ecocyc.RIBOFLAVINKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00255`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
