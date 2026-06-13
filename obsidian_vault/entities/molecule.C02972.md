---
entity_id: "molecule.C02972"
entity_type: "small_molecule"
name: "Dihydrolipoylprotein"
source_database: "KEGG"
source_id: "C02972"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dihydrolipoylprotein"
  - "[H-protein]-dihydrolipoyllysine"
  - "[GCSH]-N6-[(R)-dihydrolipoyl]-L-lysine"
  - "[GcvH]-N6-[(R)-dihydrolipoyl]-L-lysine"
  - "[Glycine cleavage system H]-N6-[(R)-dihydrolipoyl]-L-lysine"
---

# Dihydrolipoylprotein

`molecule.C02972`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02972`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dihydrolipoylprotein; [H-protein]-dihydrolipoyllysine; [GCSH]-N6-[(R)-dihydrolipoyl]-L-lysine; [GcvH]-N6-[(R)-dihydrolipoyl]-L-lysine; [Glycine cleavage system H]-N6-[(R)-dihydrolipoyl]-L-lysine EcoCyc common name: dihydrolipoamide.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: Dihydrolipoylprotein; [H-protein]-dihydrolipoyllysine; [GCSH]-N6-[(R)-dihydrolipoyl]-L-lysine; [GcvH]-N6-[(R)-dihydrolipoyl]-L-lysine; [Glycine cleavage system H]-N6-[(R)-dihydrolipoyl]-L-lysine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R04125|reaction.R04125]] `KEGG` `database` - C01242 + C00101 <=> C02972 + C00143 + C00014
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDLIPACETRANS-RXN|reaction.ecocyc.DIHYDLIPACETRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02972`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
