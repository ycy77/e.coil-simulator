---
entity_id: "molecule.C03838"
entity_type: "small_molecule"
name: "5'-Phosphoribosylglycinamide"
source_database: "KEGG"
source_id: "C03838"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5'-Phosphoribosylglycinamide"
  - "GAR"
  - "N1-(5-Phospho-D-ribosyl)glycinamide"
  - "Glycinamide ribonucleotide"
  - "N1-(5-Phospho-beta-D-ribosyl)glycinamide"
---

# 5'-Phosphoribosylglycinamide

`molecule.C03838`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03838`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5'-Phosphoribosylglycinamide; GAR; N1-(5-Phospho-D-ribosyl)glycinamide; Glycinamide ribonucleotide; N1-(5-Phospho-beta-D-ribosyl)glycinamide EcoCyc common name: N1-(5-phospho-β-D-ribosyl)glycinamide.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: 5'-Phosphoribosylglycinamide; GAR; N1-(5-Phospho-D-ribosyl)glycinamide; Glycinamide ribonucleotide; N1-(5-Phospho-beta-D-ribosyl)glycinamide

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R04144|reaction.R04144]] `KEGG` `database` - C00002 + C03090 + C00037 <=> C00008 + C00009 + C03838
- `is_product_of` --> [[reaction.ecocyc.GLYRIBONUCSYN-RXN|reaction.ecocyc.GLYRIBONUCSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R06974|reaction.R06974]] `KEGG` `database` - C00058 + C00002 + C03838 <=> C00008 + C00009 + C04376
- `is_substrate_of` --> [[reaction.ecocyc.GART-RXN|reaction.ecocyc.GART-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GARTRANSFORMYL2-RXN|reaction.ecocyc.GARTRANSFORMYL2-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03838`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
