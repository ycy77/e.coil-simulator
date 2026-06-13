---
entity_id: "molecule.C00620"
entity_type: "small_molecule"
name: "alpha-D-Ribose 1-phosphate"
source_database: "KEGG"
source_id: "C00620"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha-D-Ribose 1-phosphate"
  - "Ribose 1-phosphate"
  - "D-Ribose 1-phosphate"
---

# alpha-D-Ribose 1-phosphate

`molecule.C00620`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00620`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha-D-Ribose 1-phosphate; Ribose 1-phosphate; D-Ribose 1-phosphate EcoCyc common name: α-D-ribose-1-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: alpha-D-Ribose 1-phosphate; Ribose 1-phosphate; D-Ribose 1-phosphate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (12)

- `is_product_of` --> [[reaction.R02147|reaction.R02147]] `KEGG` `database` - C00387 + C00009 <=> C00242 + C00620
- `is_product_of` --> [[reaction.ecocyc.ADENPHOSPHOR-RXN|reaction.ecocyc.ADENPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.INOPHOSPHOR-RXN|reaction.ecocyc.INOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PNP-RXN|reaction.ecocyc.PNP-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5199|reaction.ecocyc.RXN0-5199]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URPHOS-RXN|reaction.ecocyc.URPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN|reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R08229|reaction.R08229]] `KEGG` `database` - C07649 + C00620 <=> C16633 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.PPENTOMUT-RXN|reaction.ecocyc.PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7092|reaction.ecocyc.RXN0-7092]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.THYM-PHOSPH-RXN|reaction.ecocyc.THYM-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.URPHOS-RXN|reaction.ecocyc.URPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00620`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
