---
entity_id: "molecule.C03090"
entity_type: "small_molecule"
name: "5-Phosphoribosylamine"
source_database: "KEGG"
source_id: "C03090"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Phosphoribosylamine"
  - "5-Phospho-beta-D-ribosylamine"
  - "5-Phospho-D-ribosylamine"
  - "5-Phosphoribosyl-1-amine"
---

# 5-Phosphoribosylamine

`molecule.C03090`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03090`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Phosphoribosylamine; 5-Phospho-beta-D-ribosylamine; 5-Phospho-D-ribosylamine; 5-Phosphoribosyl-1-amine EcoCyc common name: 5-phospho-β-D-ribosylamine.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Annotation

KEGG compound: 5-Phosphoribosylamine; 5-Phospho-beta-D-ribosylamine; 5-Phospho-D-ribosylamine; 5-Phosphoribosyl-1-amine

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN0-7170|reaction.ecocyc.RXN0-7170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R04144|reaction.R04144]] `KEGG` `database` - C00002 + C03090 + C00037 <=> C00008 + C00009 + C03838
- `is_substrate_of` --> [[reaction.ecocyc.GLYRIBONUCSYN-RXN|reaction.ecocyc.GLYRIBONUCSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PRPPAMIDOTRANS-RXN|reaction.ecocyc.PRPPAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLYRIBONUCSYN-RXN|reaction.ecocyc.GLYRIBONUCSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03090`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
