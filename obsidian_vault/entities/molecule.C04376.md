---
entity_id: "molecule.C04376"
entity_type: "small_molecule"
name: "5'-Phosphoribosyl-N-formylglycinamide"
source_database: "KEGG"
source_id: "C04376"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5'-Phosphoribosyl-N-formylglycinamide"
  - "N-Formyl-GAR"
  - "N-Formylglycinamide ribonucleotide"
  - "N2-Formyl-N1-(5-phospho-D-ribosyl)glycinamide"
  - "N2-Formyl-N1-(5-phospho-beta-D-ribosyl)glycinamide"
---

# 5'-Phosphoribosyl-N-formylglycinamide

`molecule.C04376`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04376`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5'-Phosphoribosyl-N-formylglycinamide; N-Formyl-GAR; N-Formylglycinamide ribonucleotide; N2-Formyl-N1-(5-phospho-D-ribosyl)glycinamide; N2-Formyl-N1-(5-phospho-beta-D-ribosyl)glycinamide EcoCyc common name: N2-formyl-N1-(5-phospho-β-D-ribosyl)glycinamide.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: 5'-Phosphoribosyl-N-formylglycinamide; N-Formyl-GAR; N-Formylglycinamide ribonucleotide; N2-Formyl-N1-(5-phospho-D-ribosyl)glycinamide; N2-Formyl-N1-(5-phospho-beta-D-ribosyl)glycinamide

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R06974|reaction.R06974]] `KEGG` `database` - C00058 + C00002 + C03838 <=> C00008 + C00009 + C04376
- `is_product_of` --> [[reaction.ecocyc.GART-RXN|reaction.ecocyc.GART-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GARTRANSFORMYL2-RXN|reaction.ecocyc.GARTRANSFORMYL2-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.FGAMSYN-RXN|reaction.ecocyc.FGAMSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04376`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
