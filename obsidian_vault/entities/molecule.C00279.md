---
entity_id: "molecule.C00279"
entity_type: "small_molecule"
name: "D-Erythrose 4-phosphate"
source_database: "KEGG"
source_id: "C00279"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Erythrose 4-phosphate"
---

# D-Erythrose 4-phosphate

`molecule.C00279`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00279`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Erythrose 4-phosphate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: D-Erythrose 4-phosphate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.SEDOBISALDOL-RXN|reaction.ecocyc.SEDOBISALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANSALDOL-RXN|reaction.ecocyc.TRANSALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.2TRANSKETO-RXN|reaction.ecocyc.2TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ERYTH4PDEHYDROG-RXN|reaction.ecocyc.ERYTH4PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN-9952|reaction.ecocyc.RXN-9952]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00279`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
