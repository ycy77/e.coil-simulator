---
entity_id: "molecule.C02630"
entity_type: "small_molecule"
name: "2-Hydroxyglutarate"
source_database: "KEGG"
source_id: "C02630"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Hydroxyglutarate"
  - "alpha-Hydroxyglutarate"
  - "2-Hydroxyglutaric acid"
---

# 2-Hydroxyglutarate

`molecule.C02630`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02630`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Hydroxyglutarate; alpha-Hydroxyglutarate; 2-Hydroxyglutaric acid

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)

## Annotation

KEGG compound: 2-Hydroxyglutarate; alpha-Hydroxyglutarate; 2-Hydroxyglutaric acid

## Pathways

- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.HYDGLUTSYN-RXN|reaction.ecocyc.HYDGLUTSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R08198|reaction.R08198]] `KEGG` `database` - C02630 + C00003 <=> C00026 + C00004 + C00080
- `represses` --> [[reaction.ecocyc.KETOGLUTREDUCT-RXN|reaction.ecocyc.KETOGLUTREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-16701|reaction.ecocyc.RXN-16701]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02630`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
