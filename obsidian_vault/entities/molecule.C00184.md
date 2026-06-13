---
entity_id: "molecule.C00184"
entity_type: "small_molecule"
name: "Glycerone"
source_database: "KEGG"
source_id: "C00184"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glycerone"
  - "Dihydroxyacetone"
  - "1,3-Dihydroxyacetone"
  - "1,3-Dihydroxy-2-propanone"
  - "1,3-Dihydroxypropan-2-one"
---

# Glycerone

`molecule.C00184`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00184`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glycerone; Dihydroxyacetone; 1,3-Dihydroxyacetone; 1,3-Dihydroxy-2-propanone; 1,3-Dihydroxypropan-2-one EcoCyc common name: dihydroxyacetone.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: Glycerone; Dihydroxyacetone; 1,3-Dihydroxyacetone; 1,3-Dihydroxy-2-propanone; 1,3-Dihydroxypropan-2-one

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.R01010|reaction.R01010]] `KEGG` `database` - C00111 + C00001 <=> C00184 + C00009
- `is_product_of` --> [[reaction.ecocyc.GLYCDEH-RXN|reaction.ecocyc.GLYCDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-313|reaction.ecocyc.RXN0-313]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7249|reaction.ecocyc.RXN0-7249]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-559|reaction.ecocyc.TRANS-RXN0-559]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01012|reaction.R01012]] `KEGG` `database` - C00074 + C00184 <=> C00022 + C00111
- `is_substrate_of` --> [[reaction.ecocyc.2.7.1.121-RXN|reaction.ecocyc.2.7.1.121-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7169|reaction.ecocyc.RXN0-7169]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-559|reaction.ecocyc.TRANS-RXN0-559]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-7390|reaction.ecocyc.RXN0-7390]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00184`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
