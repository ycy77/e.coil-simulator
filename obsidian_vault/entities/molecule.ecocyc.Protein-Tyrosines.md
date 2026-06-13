---
entity_id: "molecule.ecocyc.Protein-Tyrosines"
entity_type: "small_molecule"
name: "a [protein]-L-tyrosine"
source_database: "EcoCyc"
source_id: "Protein-Tyrosines"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "a protein tyrosine"
  - "protein tyrosine"
---

# a [protein]-L-tyrosine

`molecule.ecocyc.Protein-Tyrosines`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Protein-Tyrosines`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This compound class stands for generic and unspecified protein tyrosines. This compound class stands for generic and unspecified protein tyrosines.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Annotation

This compound class stands for generic and unspecified protein tyrosines.

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN|reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16454|reaction.ecocyc.RXN-16454]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24992|reaction.ecocyc.RXN-24992]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Protein-Tyrosines`
- `SEED:cpd11704`
- `METANETX:MNXM7713`
- `LIGAND-CPD:C00585`
